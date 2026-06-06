import random

def extract_issue_data_from_image(image_bytes: bytes) -> dict:
    """
    Mock function simulating local VLM execution.
    In a real scenario, this would use llama-cpp-python or Ollama to run inference
    on the image bytes to extract the issue type, severity, and location.
    """
    # Simulate a slightly randomized output for demonstration purposes
    issue_types = ["pothole", "graffiti", "broken_streetlight", "fly_tipping"]
    locations = ["Camden", "Westminster", "Islington", "Hackney", "Southwark", "Lambeth"]
    
    return {
        "issue_type": random.choice(issue_types),
        "severity": random.randint(1, 5),  # 1 (low) to 5 (high)
        "location": random.choice(locations),
        "description": "Auto-generated mock description based on visual analysis."
    }
