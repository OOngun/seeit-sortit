import requests
import os
from typing import Optional

def get_tfl_delay_factor(app_key: Optional[str] = None) -> float:
    """
    Fetches live road disruptions from TfL API and calculates a general delay factor.
    In a real scenario, this could take location parameters to calculate localized traffic impact.
    """
    url = "https://api.tfl.gov.uk/Road/all/Disruption"
    params = {}
    
    resolved_key = app_key or os.getenv("TFL_APP_KEY")
    if resolved_key:
        params["app_key"] = resolved_key


    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        disruptions = response.json()

        # A very basic heuristic: Count disruptions and map to a severity multiplier.
        # Assume an average baseline of e.g. 50 active disruptions = 1.0 factor.
        # This will scale the priority based on how busy/disrupted the routes are.
        disruption_count = len(disruptions)
        
        # We can cap the factor between 0.5 (low disruption) and 3.0 (high disruption)
        base_factor = disruption_count / 50.0
        return max(0.5, min(3.0, base_factor))

    except Exception as e:
        print(f"Failed to fetch TfL data: {e}")
        # Default delay factor if API fails
        return 1.0
