# Solar PV on Landfills (Atlanta MSA)
 
A command-line tool for identifying solar photovoltaic installations sited on landfills within the Atlanta MSA, using the [U.S. Large-Scale Solar Photovoltaic Database (USPVDB)](https://eerscmap.usgs.gov/uspvdb/).
 
## What it does
 
The script takes a raw USPVDB CSV export and:
 
1. **Filters to Georgia**, then to a hardcoded list of Atlanta MSA counties.
2. **Filters to landfill sites**: projects where USPVDB's `p_type` field is `landfill` or `landfill named`.
3. **Prints summary statistics** to the console:
   - Names of landfills with solar PV systems installed
   - Cumulative count of landfill solar PV sites as of several benchmark years
   - Total installed solar PV capacity across those sites, in MW AC
4. **Saves the filtered dataset** as a CSV for further use.
## Requirements
 
- Python 3.8+
- Packages: `pandas`
Install with:
 
```bash
pip install pandas
```
 
## Getting the input data
 
Download a CSV export of the USPVDB from the [USGS USPVDB site](https://eerscmap.usgs.gov/uspvdb/data/). Save it locally since you'll pass its path as an argument.
 
The script expects these columns to be present: `p_name`, `p_county`, `p_year`, `p_state`, `p_sys_type`, `p_type`, `p_cap_ac`, `p_cap_dc`. A standard USPVDB export should already contain all of these — if any are missing, the script will print a warning listing what's absent but will still attempt to run (this only becomes a hard failure if a step further down actually needs one of the missing columns).
 
## Basic usage
 
```bash
python solar-PV-landfills.py path/to/uspvdb.csv
```
 
## Command-line options
 
| Argument | Required? | Default | Description |
|---|---|---|---|
| `csv_path` | Yes | — | Path to the USPVDB CSV file (e.g. `uspvdb_v4_2026.04.14.csv`). |
 
## Examples
 
**Run with defaults:**
```bash
python solar-PV-landfills.py uspvdb_v4_2026.04.14.csv
```
 
## Outputs
 
- **Console output**: names of landfills with solar PV systems installed, a table of cumulative landfill solar PV site counts at the benchmark years (2005, 2015, 2025, 2026), plus total installed AC capacity across all matched sites.
- **A filtered CSV** (`atlanta_msa_solar_pv_landfills.csv`, saved to the current directory): one row per landfill solar PV site in the Atlanta MSA, with all original USPVDB columns retained.


## Notes on the data

- **County list is hardcoded.** The Atlanta MSA county list lives as a Python list (`atlanta_msa_counties`) near the top of the script, not pulled from a live boundary source. If ARC updates the MSA county composition, this list needs to be edited by hand.
- **County matching is case-insensitive** and handles `DeKalb`'s internal capitalization correctly (the script deliberately skips `.str.title()` on the county column for this reason).
- **`p_year` is coerced to numeric**, so any USPVDB rows with a non-numeric or missing year will be excluded from the cumulative-count table (though they're still included in the total capacity figure and the saved CSV).
