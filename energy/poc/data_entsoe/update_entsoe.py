import pandas as pd
from entsoe import EntsoePandasClient

TAGS_RENEW: dict[str, str] = {
    "Biomass": "Biomass",
    "Geothermal": "Geothermal",
    "Hydro_storage": "Hydro Pumped Storage",
    "Hydro": "Hydro Run-of-river and poundage",
    "Hydro_res": "Hydro Water Reservoir",
    "Other_renew": "Other renewable",
    "Solar": "Solar",
    "Wind_off": "Wind Offshore",
    "Wind_on": "Wind Onshore",
}

TAGS_NON_RENEW: dict[str, str] = {
    "Lignite": "Fossil Brown coal/Lignite",
    "Gas": "Fossil Gas",
    "Coal": "Fossil Hard coal",
    "Oil": "Fossil Oil",
    "Nuclear": "Nuclear",
    "Other": "Other",
    "Waste": "Waste",
}
ALL_TAGS: dict[str, str] = TAGS_NON_RENEW | TAGS_RENEW

def process_generation(generation_raw):
    # process
    if isinstance(generation_raw.columns, pd.MultiIndex):
        generation_raw.columns = generation_raw.columns.droplevel(level=1)

    # remove duplicated columns
    generation_raw = generation_raw.loc[:, ~generation_raw.columns.duplicated()].copy()

    # If the data is in 15-minute intervals, resample it to 1-hour intervals (for weather)
    time_diff = generation_raw.index.to_series().diff().min()
    if time_diff == pd.Timedelta(minutes=15):
        generation_raw = generation_raw.resample('h').mean()

    # create a new data frame based on raw data
    generation_processed: pd.DataFrame = pd.DataFrame(
        index=generation_raw.index,
        columns=ALL_TAGS.keys(),
    )

    # create a new data frame based on raw data
    for k, v in ALL_TAGS.items():  # iterate over all production types
        # if the production type is not available, assume the production is 0
        if v in generation_raw.columns:
            generation_processed[k] = generation_raw[v]
        else:
            generation_processed[k] = 0.0
    generation_processed = generation_processed.fillna(0.0)
    generation_processed["Renewables"] = generation_processed[list(TAGS_RENEW)].sum(axis=1)
    generation_processed["NonRenewables"] = generation_processed[list(TAGS_NON_RENEW)].sum(axis=1)
    generation_processed["Total"] = generation_processed["NonRenewables"] + generation_processed["Renewables"]
    return generation_processed

def fetch_data_entsoe(start, end, country_code, country_code_prices, api_key):
    # get entso-e client
    client = EntsoePandasClient(api_key=api_key)
    # get generation
    generation_raw: pd.DataFrame = client.query_generation(
        country_code=country_code, start=start, end=end
    )
    # process generation
    generation_processed = process_generation(generation_raw)

    # Get load
    load_raw: pd.DataFrame = client.query_load(
        country_code=country_code, start=start, end=end)

    # If the data is in 15-minute intervals, resample it to 1-hour intervals (for weather)
    time_diff = load_raw.index.to_series().diff().min()
    if time_diff == pd.Timedelta(minutes=15):
        load_raw = load_raw.resample('h').mean()

    # get Day-ahead prices
    prices_raw = []
    for country_code_price in country_code_prices:
        prices_raw_de_at_lu: pd.DataFrame = client.query_day_ahead_prices(
            country_code=country_code_price, start=start, end=end)
        prices_raw_de_at_lu = prices_raw_de_at_lu.to_frame()
        prices_raw_de_at_lu = prices_raw_de_at_lu.rename(columns={0: 'Day Ahead Price'})
        prices_raw.append(prices_raw_de_at_lu)
    prices_raw = pd.concat(prices_raw, axis=0)

    # concatanate all data
    data = pd.concat([generation_processed, load_raw, prices_raw], axis=1)

    # Convert to UTC (use the same format as in weather data)
    data = data.reset_index().rename(columns={"index":"date"})
    data['datetime_utc'] = data['date'].dt.tz_convert('UTC')
    data['dt_iso'] = data['datetime_utc'].dt.strftime("%Y-%m-%d %H:%M:%S %z UTC")
    data.drop(labels=['datetime_utc','date'], axis=1, inplace=True)
    data.dropna(inplace=True)

    return data

