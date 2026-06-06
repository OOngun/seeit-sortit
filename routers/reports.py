from fastapi import APIRouter, File, UploadFile, Depends
from typing import Optional

from services.vlm_service import extract_issue_data_from_image
from services.tfl_service import get_tfl_delay_factor
from services.datastore_service import get_population_density
from services.scoring_service import calculate_priority_score

router = APIRouter()

@router.post("/submit-report")
async def submit_report(
    image: UploadFile = File(...),
    tfl_app_key: Optional[str] = None
):
    """
    Ingests a citizen report (image) of a city issue.
    Runs it through local VLM, enriches with static CSV data and live TfL data,
    and returns a deterministic priority score.
    """
    
    # 1. Read Image
    image_bytes = await image.read()
    
    # 2. Extract data via Local VLM
    vlm_data = extract_issue_data_from_image(image_bytes)
    
    # 3. Enrich with Live API data (TfL)
    tfl_delay_factor = get_tfl_delay_factor(app_key=tfl_app_key)
    
    # 4. Enrich with Static CSV data (Population Density)
    population_density = get_population_density(vlm_data["location"])
    
    # 5. Calculate Priority Score
    priority_score = calculate_priority_score(
        vlm_severity=vlm_data["severity"],
        tfl_delay_factor=tfl_delay_factor,
        population_density=population_density,
        issue_type=vlm_data["issue_type"]
    )
    
    # 6. Return Final Payload
    return {
        "status": "success",
        "priority_score": round(priority_score, 2),
        "details": {
            "vlm_analysis": vlm_data,
            "enrichment": {
                "tfl_delay_factor": round(tfl_delay_factor, 2),
                "population_density": population_density
            }
        }
    }
