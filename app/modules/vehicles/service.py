from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db

from .repository import VehicleRepository


def get_vehicle_repository(
    db: Session = Depends(get_db)
):
    return VehicleRepository(db)


class VehicleService:

    def __init__(self, repository: VehicleRepository):
        self.repository = repository

    def get_companies(self):
        companies = self.repository.get_companies()

        return [
            {
                "name": company.name
            }
            for company in companies
        ]

    def get_models_by_company(self, company: str):
        models = self.repository.get_models_by_company(company)

        return [
            {
                "name": model.name
            }
            for model in models
        ]


def get_vehicle_service(
    repository: VehicleRepository = Depends(get_vehicle_repository)
):
    return VehicleService(repository)