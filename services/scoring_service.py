# Define some baseline costs for fixing issues
BASELINE_COSTS = {
    "pothole": 200.0,
    "graffiti": 50.0,
    "broken_streetlight": 500.0,
    "fly_tipping": 150.0
}

def calculate_priority_score(vlm_severity: float, tfl_delay_factor: float, population_density: float, issue_type: str) -> float:
    """
    Calculates a deterministic priority score using the exact formula:
    Priority Score = ((VLM_Severity * TfL_Delay_Factor) * Population_Density) / Baseline_Cost
    """
    # Get the baseline cost, defaulting to 100.0 if not found
    baseline_cost = BASELINE_COSTS.get(issue_type, 100.0)
    
    # Avoid division by zero
    if baseline_cost <= 0:
        baseline_cost = 1.0

    score = ((vlm_severity * tfl_delay_factor) * population_density) / baseline_cost
    return score
