import pandas as pd
import os

DENSITY_CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "density.csv")

# Initialize the fast lookup dictionary
_density_lookup = {}

def load_density_data():
    """
    Loads the density.csv file into a fast dictionary lookup.
    """
    global _density_lookup
    try:
        df = pd.read_csv(DENSITY_CSV_PATH)
        # Assuming the CSV has columns 'Location' and 'Population_Density'
        _density_lookup = df.set_index('Location')['Population_Density'].to_dict()
        print("Successfully loaded density datastore.")
    except Exception as e:
        print(f"Warning: Failed to load density data: {e}")

def get_population_density(location: str) -> float:
    """
    Retrieves the population density for a given location.
    Defaults to a standard value if location is unknown.
    """
    if not _density_lookup:
        load_density_data()
    
    # Return a default value of 10000 if not found
    return _density_lookup.get(location, 10000.0)
