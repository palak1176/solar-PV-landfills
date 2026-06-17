# Atlanta MSA Solar Landfill Analysis
This project processes utility-scale solar photovoltaic (PV) data from the U.S. PV Database (USPVDB) and identifies solar PV landfill sites located within the Atlanta Metropolitan Statistical Area (MSA). The script filters and cleans USPVDB data, isolates landfill solar projects in Atlanta MSA counties, calculates cumulative site counts over time, and summarizes installed solar PV capacity on landfill sites.

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
- Computes total installed solar PV capacity on Atlanta MSA landfill sites (MW AC)
- Stores results in a pandas DataFrame
- Exports filtered landfill solar PV data to a CSV file

## Technologies Used
- Python 3
- Pandas

## Input Data
- The script expects a CSV file from the U.S. PV Database (USPVDB)

## Output Data
- The script generates a CSV file containing landfill-based solar PV projects located within the Atlanta MSA
- Output data includes: project name, county, installation year, system type, project type, AC capacity (MW), DC capacity (MW)
- The script also prints the cumulative landfill solar PV site counts by year and the total installed AC solar PV capacity on landfill sites within the Atlanta MSA
- Review the cumulative site counts and capacity summary printed to the console
- Open the generated CSV file for additional analysis or visualization

## Usage
- Install required packages: pip install pandas
- Download the USPVDB CSV file from [https://energy.usgs.gov/uspvdb/data/](url).
- Place the CSV file in the same folder as your Python script.
- If needed, replace the filename at the end of the script: print(uspvdb_solar_ga_data("uspvdb_v4_2026.04.14.csv"))
- Run the script: python solar_PV_landfills.py
