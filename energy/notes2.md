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
	- [Python](https://pypi.org/project/entsoe-py/)
	- [github](https://github.com/EnergieID/entsoe-py)
	- [info](https://thesmartinsights.com/how-to-query-data-from-the-entso-e-transparency-platform-using-python/)
	- Projects that use it: 1., 2.
	- API keys found
		- 94aa148a-330b-4eee-ba0c-8a5eb0b17825
		- c93c7111-9e18-49be-b42c-ceeed9aabfb2
		- 6e68642c-8403-4caa-af31-bda40b8c67f6
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

1. [derevirn/renewcast](https://github.com/derevirn/renewcast)
	- [app](http://renewcast.giannis.io/)
	- APP; pulls from ENTSOE; forecasts ARIMA; simple app
	
2. [Helmholtz-AI-Energy/electric-generation-forecasting](https://github.com/Helmholtz-AI-Energy/electric-generation-forecasting)
	- [enhanced-load-forecasting](https://www.entsoe.eu/Technopedia/techsheets/enhanced-load-forecasting)
	- Full PyTorch ML model with API pullind data and forcasting with LSTM architecture and [SARIMA](pip install pmdarima)
	- Extremely well documented
	- API key used: 6e68642c-8403-4caa-af31-bda40b8c67f6
	
---

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

