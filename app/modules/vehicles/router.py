from fastapi import APIRouter, Depends, HTTPException

from .schemas import CompanyResponse, ModelResponse
from .service import VehicleService, get_vehicle_service


router = APIRouter(
    prefix="/vehicles",
    tags=["Vehicles"]
)


@router.get(
    "/companies",
    response_model=list[CompanyResponse]
)
def get_companies(
    service: VehicleService = Depends(get_vehicle_service)
):
    return service.get_companies()


@router.get(
    "/companies/{company}/models",
    response_model=list[ModelResponse]
)
def get_models(
    company: str,
    service: VehicleService = Depends(get_vehicle_service)
):
    models = service.get_models_by_company(company)

    if not models:
        raise HTTPException(
            status_code=404,
            detail="Company not found or has no models"
        )

    return models