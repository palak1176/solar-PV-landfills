import pandas as pd

atlanta_msa_counties = [
    "Barrow", "Clayton", "Douglas", "Haralson", "Meriwether", 
    "Pike", "Bartow", "Cobb", "Fayette", "Heard", "Morgan", 
    "Rockdale", "Butts", "Coweta", "Forsyth", "Henry", "Newton", 
    "Spalding", "Carroll", "Dawson", "Fulton", "Jasper", "Paulding", 
    "Walton", "Cherokee", "DeKalb", "Gwinnett", "Lumpkin", "Pickens"]

def uspvdb_solar_ga_data(file_path):
    # Reads CSV file
    try:
        uspvdb_solar_ga_df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: There was a parsing error while reading the file.")
        return None
    
    # print(uspvdb_solar_ga_df.columns)
    
    # Check for required columns and keep only those needed for analysis
    columns_to_keep = ['p_name', 'p_county', "p_year", 'p_state', 'p_sys_type', 'p_type'] 
    # could include p_area 

    missing_cols = [col for col in columns_to_keep if col not in uspvdb_solar_ga_df.columns]
    if missing_cols:
        print(f"Missing columns: {missing_cols}")
    uspvdb_solar_ga_df = uspvdb_solar_ga_df[columns_to_keep]

    # Clean and filter data for Georgia
    uspvdb_solar_ga_df['p_state'] = uspvdb_solar_ga_df['p_state'].fillna('').str.strip().str.upper()
    uspvdb_solar_ga_df = uspvdb_solar_ga_df[uspvdb_solar_ga_df['p_state'] == 'GA']

     # Clean 'p_county' column and filter for Atlanta MSA counties
    uspvdb_solar_ga_df['p_county'] = uspvdb_solar_ga_df['p_county'].fillna('').str.strip() # can't do title case because of "DeKalb"
    # Case-insensitive filter
    atlanta_msa_counties_lower = {c.lower() for c in atlanta_msa_counties}
    uspvdb_solar_ga_df = uspvdb_solar_ga_df[uspvdb_solar_ga_df['p_county'].str.lower().isin(atlanta_msa_counties_lower)]


    # Clean 'p_type' column and filter for landfill named or landfill
    uspvdb_solar_ga_df['p_type'] = uspvdb_solar_ga_df['p_type'].fillna('').str.strip().str.lower()
    uspvdb_solar_ga_df = uspvdb_solar_ga_df[uspvdb_solar_ga_df['p_type'].isin(['landfill named', 'landfill'])]    

    # # Calculate and print the number of solar PV landfill sites by type
    # uspvdb_solar_ga_types = uspvdb_solar_ga_df.groupby('p_type').size().reset_index(name='Count')
    # print("\nSolar PV Landfill Sites by Type:")
    # for _, row in uspvdb_solar_ga_types.iterrows():
    #     print(f"Type: {row['p_type']}, Count: {row['Count']}")
    
    print("\nCumulative Solar PV Landfill Sites Over Time")

    # Years to evaluate
    target_years = [2005, 2015, 2025, 2026]

    # Ensure p_year is numeric
    uspvdb_solar_ga_df['p_year'] = pd.to_numeric(uspvdb_solar_ga_df['p_year'],errors='coerce')

    # Build cumulative counts
    cumulative_counts = []

    for year in target_years:
        count = uspvdb_solar_ga_df[
            uspvdb_solar_ga_df['p_year'] <= year
        ].shape[0]

        cumulative_counts.append({
            'Year': year,
            'Cumulative Site Count': count
        })

    # Convert to DataFrame
    uspvdb_solar_ga_years = pd.DataFrame(cumulative_counts)

    # Print table
    print(uspvdb_solar_ga_years.to_string(index=False))

    return uspvdb_solar_ga_df
    # .to_csv("atlanta_msa_solar_pv_sites.csv", index=False)

print(uspvdb_solar_ga_data("uspvdb_v4_2026.04.14.csv"))
