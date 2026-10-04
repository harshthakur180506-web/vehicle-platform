from fastapi import FastAPI

from app.modules.vehicles.router import router as vehicles_router

app = FastAPI(
    title="Vehicle API", 
    version="1.0.0")

app.include_router(
    vehicles_router, 
    prefix="/vehicles")

@app.get("/")
def root():
    return {"message": "Vehicle platform API is up and running!"}
