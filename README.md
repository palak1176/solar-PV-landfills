# Atlanta MSA Solar Landfill Analysis
This project processes utility-scale solar photovoltaic (PV) data from the U.S. PV Database (USPVDB) and identifies solar PV landfill sites located within the Atlanta Metropolitan Statistical Area (MSA). The script filters raw CSV data, cleans and standardizes values, handles missing data, and calculates cumulative counts of landfill-based solar PV sites over time

## Features
- Loads USPVDB solar PV data from a CSV file
- Handles common file-reading errors
- Checks for required columns before analysis
- Cleans and standardizes state values
- Filters data to only include Georgia (GA)
- Cleans and standardizes county names
- Filters data to only include Atlanta MSA counties
- Cleans and standardizes project type values
- Filters projects to only include landfill and landfill named
- Computes cumulative landfill solar PV site counts for selected years: 2005, 2015, 2025, 2026
- Returns a cleaned pandas DataFrame for further analysis

## Technologies Used
- Python 3
- Pandas

## Input Data
- The script expects a CSV file from the U.S. PV Database (USPVDB) containing at least the following columns:
  - p_name
  - p_county
  - p_year
  - p_state
  - p_sys_type
  - p_type

  ## Usage
  - Download the USPVDB CSV file from [https://energy.usgs.gov/uspvdb/data/](url).
  - Place the CSV file in the same folder as your Python script.
  - If needed, replace the filename at the end of the script: print(uspvdb_solar_ga_data("uspvdb_v4_2026.04.14.csv"))
  - Run the script: python solar_PV_landfills.py
