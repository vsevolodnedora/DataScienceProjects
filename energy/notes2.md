# ALL DATA
[Jcharis/DataScienceTools](https://github.com/Jcharis/DataScienceTools)
[bchapuis/awesome-spatial-data](https://github.com/bchapuis/awesome-spatial-data)

---

# Lecures and course 
1. [pitmonticone/EnergySystemModelling](https://github.com/pitmonticone/EnergySystemModelling)
	- Resources for the Energy System Modelling course by Tom Brown at Karlsruhe Institute of Technology (2020).
	- 12 videos on utube
	
2. [fneum/data-science-for-esm](https://github.com/fneum/data-science-for-esm)
	- course on Data Science for Energy System Modelling (Course at TU Berlin to learn energy system modelling with data)
	- Main contributor to Python for Power System Analysis [Git](https://github.com/PyPSA) and [Web](https://pypsa.org/)
	- [INTRODUCTIONS](https://fneum.github.io/data-science-for-esm/intro.html)
	
3. [PacktPublishing/Modern-Time-Series-Forecasting-with-Python](https://github.com/PacktPublishing/Modern-Time-Series-Forecasting-with-Python)	
	- Repo from [book](https://www.packtpub.com/en-us/product/modern-time-series-forecasting-with-python-9781803246802)
	- Modern Time Series Forecasting with Python, published by Packt
	- Explore industry-ready time series forecasting using modern machine learning and deep learning
	
4. [thuml/Time-Series-Library](https://github.com/thuml/Time-Series-Library/)
	- A Library for Advanced Deep Time Series Models.
	- Extension of [Autoformer](https://github.com/thuml/Autoformer) [paper](https://arxiv.org/abs/2106.13008)
	
5. [Capsar/The-Rise-of-Diffusion-Models-in-Time-Series-Forecasting](https://github.com/Capsar/The-Rise-of-Diffusion-Models-in-Time-Series-Forecasting)
	- Literature Survey about the available Diffusion Models capable of Time-Series Forecasting [paper](arxiv.org/abs/2401.03006) [revewPaper](arXiv:2407.13278)

---

# Data sources
[ENTSNOE](https://transparency.entsoe.eu/dashboard/show)
	- Sources: 
		- [statistics](https://www.entsoe.eu/data/power-stats/)
	- [python API](https://pypi.org/project/entsoe-py/) [github](https://github.com/EnergieID/entsoe-py)
	- [python API with prices](https://pypi.org/project/entsoe-client/) [github](https://github.com/DarioHett/entsoe-client)
	- [info](https://thesmartinsights.com/how-to-query-data-from-the-entso-e-transparency-platform-using-python/)
	- Projects that use it: 1., 2.
	- API keys found
		- 94aa148a-330b-4eee-ba0c-8a5eb0b17825
		- c93c7111-9e18-49be-b42c-ceeed9aabfb2s
	- Repos: 7.

[JAO](https://www.jao.eu/) [jao-api](https://www.jao.eu/page-api/market-data) 
	- Cross-border electricity capacity allocation in Europe
	- [python](https://pypi.org/project/jao-py/)
	- API key reqTocken: c93c7111-9e18-49be-b42c-ceeed9aabfb2
	
[elia](https://www.elia.be/en/)
	- [Python](https://pypi.org/project/elia-py/)
	
[smard]()
	- [pyhton](https://pypi.org/project/de-smard/)
	- get data example: [git](https://github.com/shroominic/smard-api)
	- [github](https://github.com/bundesAPI/smard-api)

[energyquantified](https://www.energyquantified.com/)
	- [python](https://pypi.org/project/energyquantified/)
	- [git](https://github.com/energyquantified/eq-python-client)

[climate.copernicus](https://cds.climate.copernicus.eu/cdsapp#!/home)
	- Climate data with an [API](https://cds.climate.copernicus.eu/api-how-to#install-the-cds-api-key) in [Python](https://pypi.org/project/cdsapi/)
	- Repos: 10

[morningstarcommodity](https://mp.morningstarcommodity.com)
	- Power enterprise analysis with quality market data and automation tools
	- LoginDetails = requests.auth.HTTPBasicAuth('euli-sege@airliquide.com', 'brkGovTexY') From Project 12; MorningStar.py file

[downloads/110m-cultural-vectors](https://www.naturalearthdata.com/downloads/110m-cultural-vectors/)
	- Data for geopandas about countires: 
	- Free vector and raster map data at 1:10m, 1:50m, and 1:110m scales

## Historic (not updated data)

[pvg_tools](https://re.jrc.ec.europa.eu/pvg_tools/en/#HR)
	- Solar energy on a map

---

# Energy projects apps

1. [pekkon/EnergiaDataApp](https://github.com/pekkon/EnergiaDataApp)
	- EnergiaDataApp is a tool to look into Finnish wind power and other power system data
	- Multipage app
---

# Energy projects with ENTSOE data

## Project to check: 1,2,15,18,20,22,(24),(32),(33),37
## Aps: 28,29,30

1. [derevirn/renewcast](https://github.com/derevirn/renewcast)
	- [app](http://renewcast.giannis.io/)
	- APP; pulls from ENTSOE; forecasts ARIMA; simple app
	
2. [Helmholtz-AI-Energy/electric-generation-forecasting](https://github.com/Helmholtz-AI-Energy/electric-generation-forecasting)
	- [enhanced-load-forecasting](https://www.entsoe.eu/Technopedia/techsheets/enhanced-load-forecasting)
	- Full PyTorch ML model with API pullind data and forcasting with LSTM architecture and [SARIMA](pip install pmdarima)
	- Extremely well documented
	- API key used: 6e68642c-8403-4caa-af31-bda40b8c67f6
	
3. [Deutschiftland/energiewende-entsoe-data](https://github.com/Deutschiftland/energiewende-entsoe-data)
	- Data from 2015 to 2023 for CO2 and energy pulled with API, plotted
	
4. [CRCDApp/REN4KAST](https://github.com/CRCDApp/REN4KAST) 
	- Data in real-time (generation); wind and solar from URLs; ARIMA foracast using recent times (got API entsoe key there)
	
5. [dafrie/lstm-load-forecasting](https://github.com/dafrie/lstm-load-forecasting)
	- Old Repo. Energy, weather, etc. Many forcasting techniques. Uses darksky api (outdated)
	
6. [timweisbarth/attention-based-energy-forecasting](https://github.com/timweisbarth/attention-based-energy-forecasting)
	- New; complex; academic; advancec modeling; NO DATA SOURCES
	
7. [Open-Power-System-Data/time_series](https://github.com/Open-Power-System-Data/time_series)
	- Discussess ENTSNOE data analysis; VERY good documentation
	
8. [DominikBurkert/Microgrid_EnergyLab](https://github.com/DominikBurkert/Microgrid_EnergyLab)
	Data from static webpage from German company? Using solar energy data from another page
	- [data](https://www.ggv-energie.de/cms/netz/allgemeine-daten/netzbilanzierung-download-aller-profile.php)
	- [PHOTOVOLTAIC GEOGRAPHICAL INFORMATION SYSTEM](https://re.jrc.ec.europa.eu/pvg_tools/en/#HR)
	
9. [Bench-amblee/solar_power_prediction_model](https://github.com/Bench-amblee/solar_power_prediction_model)
	- Using data for indean solar power plants predict their generation; NO DATA DOWNLOAD

10. [qnlzgl/graphcast](https://github.com/qnlzgl/graphcast)

11. [INESCTEC/interoperable-recommender-tso](https://github.com/INESCTEC/interoperable-recommender-tso)
	- The Interoperable Recommender is a data-driven solution aimed at enabling the participation of consumers in enhancing the resilience of the European energy infrastructure.
	- Large Repo with a lot of code and documentation
	
12. [Guillaume-dcs/Project](https://github.com/Guillaume-dcs/Project)
	- Project by [Guillaume de Certaines](https://www.linkedin.com/in/guillaume-de-certaines-460088147/)
	- Plotting data from ENTSOE, morningstarcommodity. 
	- Providing figures and analysis of the global energy markets.
	
13. [MathiasSteilen/RWE-ETH-Power-Trading](https://github.com/MathiasSteilen/RWE-ETH-Power-Trading)
	- ETH Zurich Statistics Lab: Collaborating with RWE on European Cross Border Power Trading
	- Examples on loading / visualizing data; Large Repo
	
14. [Guli-Y/ElectricityPricePredictor](https://github.com/Guli-Y/ElectricityPricePredictor)
	- Developed a time series model for forecasting day-ahead electricity prices of biding zone DK1 (Denmark) using data from Entsoe and OpenWeatherMap. Model performance is evaluated using walk-forward validation and MAPE/MASE
	
15. [afshinfaramarzi/Energy-Demand-electricity-price-Forecasting](https://github.com/afshinfaramarzi/Energy-Demand-electricity-price-Forecasting)
	- Electricity price (energy demand) forecasting using different ML, DL, stacked DL and hybrid methods (XGBoost, GRU, LSTM, CNN, CNN-LSTM, LSTM-Attention, Hybrid GRU-XGBoost and Hybrid LSTM-Attention-XGBoost)..
	- Uses ENTSO-E, openweather, and Spanish TSO data
	- VERY GOOD EDA

16. [JonJae/TimeSeriesPrediction_FeedInMngmt](https://github.com/JonJae/TimeSeriesPrediction_FeedInMngmt)
	- Prediction of Renewable Power Loss caused by Feed-in Management Events
	- Final project at the Data Science Bootcamp @neuefische. This project has been developed in 4 weeks in the fall of 2020 by Tjade Appel (LinkedIn / GitHub) and Jonas Jaenicke (LinkedIn / GitHub). Please feel free to contact us.
	- NO DATA ; wery good EDA ; targreted to a single windmill

17. [MohamedAitHassoun/Predictions-of-solar-energy-production-using-the-LSTM-model-with-an-attention-mechanism](https://github.com/MohamedAitHassoun/Predictions-of-solar-energy-production-using-the-LSTM-model-with-an-attention-mechanism)
	- Predictions of Solar Energy Production Using the LSTM Model with an Attention Mechanism
	- Uses 50Hertz data pulled from their page via http
	
18. [pohlchri/transformer_time_thesis](https://github.com/pohlchri/transformer_time_thesis)
	- Potential of transformer time series models for the energy sector - Master's Thesis by Christin Pohl
	- STATIC Data from [OpenPowerSystemData](https://data.open-power-system-data.org/time_series/2020-10-06) file: time_series_60min_singleindex.csv 
	- Data was prepared using [GitHub](https://github.com/Open-Power-System-Data/time_series)
	
19. [JulesJ1/Energy_Consumption_Forecasting](https://github.com/JulesJ1/Energy_Consumption_Forecasting)
	- Forecasting Energy Consumption Using Machine Learning
	- Uses ENTSO-E and openweather to get data (no keys) ; NO DOCUMENTATION ; WITH APP	
	
20. [tightdelay/Short_Term_Carbon_Intensity_Forecasting](https://github.com/tightdelay/Short_Term_Carbon_Intensity_Forecasting)
	- Keywords: smart home, carbon emissions, forcasting, temporal fusions transformers, 50Hertz, Aprion, Tennet, Transnet
	- This thesis focuses on predicting carbon intensity across the four German Transmission System Operators (TSO) zones: 50Hertz, Amprion, Tennet, and TransnetBW. The data sets are enriched by weather and market price data.
	- a lot of notebooks
	
21. [https://github.com/DarioHett/entsoe-client](entsoe-client)
	- Formulate human-readable queries and retrieve data from ENTSO-E into pandas.DataFrame format.
	- Allows to get a day-ahead electricity price [USE AS A LIBRARY](https://pypi.org/project/entsoe-client/)
	
22. [Fastjur/S.C.A.L.E.](https://github.com/Fastjur/S.C.A.L.E.) 
	- S.C.A.L.E. (Scheduler for Carbon-Aware Load Execution) [thesis](https://repository.tudelft.nl/record/uuid:79406c06-ab43-4cba-9136-cb8243e891ed)
	- Pulls weather data from ENTSOE!
	
23. [PyPSA/powerplantmatching](https://github.com/PyPSA/powerplantmatching)
	- A toolset for cleaning, standardizing and combining multiple power plant databases.
	
24. [KIT-IAI/Transformer-Networks-for-Electrical-Load-Time-Series-Forecasting](https://github.com/KIT-IAI/Transformer-Networks-for-Electrical-Load-Time-Series-Forecasting)
	- forcasting energy market using transformer architectures (MASTER THESIS) [analysis of ATTENTION model]
	- uses static, 'open-power-system-data' data from 2020

25. [olemagnp/entsoeAPI](https://github.com/olemagnp/entsoeAPI)
	- Entsoe Day-Ahead Electricity Price Fetcher
	- Uses FOREX and ENTISE XML files to get prices, no examples, just a library for APIs

26. [jrajaniemi/Spot](https://github.com/jrajaniemi/Spot)
	- Simple single python file to get prices from A44 form from ENTSO-E platform
	
27. [ElisNycander/nordic_model](https://github.com/ElisNycander/nordic_model)
	- Huge code to model energy grid dispatch
	- This is ODIN, an Open DIspatch model for the Nordic power system. More details of the model are provided in [1]. If you use the whole or parts of the model, please cite the paper.
	- [paper](https://www.sciencedirect.com/science/article/pii/S2211467X21001589?via%3Dihub)

28. [mt7180/energy-dashboard](https://github.com/mt7180/energy-dashboard)
	- A project to visualize power generation data for the pan-European market obtained from ENTSO-E and Energy_Charts. A streamlit, plotly, pandas, httpx/ trio (async requests) project.
	- beautifl app taht uses ENTSO-E data (custom requests) 
	- not released

29. [derevirn/renewcast](https://github.com/derevirn/renewcast)
	- [fotk](https://github.com/Aquilescool/renewcast)
	- Simple, documented, but old app deployed on streamlit
	- A web app that provides forecasts for renewable energy generation of EU countries, based on Streamlit and sktime. The app has been deployed on Heroku (does not work)
	- [meidum](https://towardsdatascience.com/forecasting-renewable-energy-generation-with-streamlit-and-sktime-ab789ef1299f)
	
30. [aurlien/motstrom](https://github.com/aurlien/motstrom)
	- uses entsoe-client to fetch prices from documents
	- exptremely simple, not deployable
	
31. [afry/energy-trading-simulator](https://github.com/afry/energy-trading-simulator)
	- Energy trading simulator developed by AFRY for the Jonstaka research project
	- This projects simulates energy trades within a local energy community (LEC). It has been developed for a research project funded by Energimyndigheten, focusing on a planned development by Tornet Bostadsproduktion AB, at Jonstaka in Varberg, Sweden.
	- HIGE repositiry
	
32. [AyrtonB/Merit-Order-Effect](https://github.com/AyrtonB/Merit-Order-Effect)
	- Code and analysis used for calculating the merit order effect of renewables on price and carbon intensity of electricity markets
	- has notebooks that download data and analyze it with explanations
	- also uses [energy-charts](https://energy-charts.info/index.html?l=en&c=DE)
	
33. [NOWUM/entso-monitor](https://github.com/NOWUM/entso-monitor)
	- ENTSO-E and ENTSO-G (gas) Monitor; This is a software project developed for the AMI Master at FH Jülich
	- Downloads and analysis data from these platforms
	- see notebooks
	- see also [berthubert/gazproject](https://github.com/berthubert/gazproject) for the use of Entose-G
	- entso-g also has a python API [nhcb/entsog-py](https://github.com/nhcb/entsog-py)

34. [freol35241/esther](https://github.com/freol35241/esther)
	- Has examples of nordpool API calls (only Sweden)
	- Esther is an Economically Smart Thermostat which runs continuous, online optimizations using a Model Predictive Control (MPC) scheme to minimize your heating cost.
	
35. [Carterbouley/ElectricityPricePrediction](https://github.com/Carterbouley/ElectricityPricePrediction)
	- Day Ahead Electricity Price Prediction
	- Also uses Coal; Natural Gas; Uranium; Oil
	- Old project; GOOD EDA

36. [piekarsky/Short-Term-Electricity-Price-Forecasting-at-the-Polish-Day-Ahead-Market](https://github.com/piekarsky/Short-Term-Electricity-Price-Forecasting-at-the-Polish-Day-Ahead-Market)
	- This repository contains the experimental source code for short term (24 hour advance) electricity price forecasting at the Polish SPOT (Day-Ahead-Market) market including RNN, LSTM, GRU, MLP and Prophet models.
Models using both the delayed exogenous variable and the endogenous variables from the forecast period and their delayed values for forecasting.
	
37. [vividfog/nordpool-predict-fi](https://github.com/vividfog/nordpool-predict-fi)
	- This is a Python app that predicts electricity prices for the Nordpool FI market. It fetches a 5-day weather forecast and more, and uses them to predict future Nordpool FI electricity prices, using a trained Random Forest model.
	- [app](https://sahkovatkain.web.app/)
	- very well developed project. Uses random forest to forcast prices
