from fastapi import FastAPI
from routers import reports

app = FastAPI(title="Zero-Cloud Council Prioritization Engine")

app.include_router(reports.router)

@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "Zero-Cloud Prioritization Engine is running locally."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
