from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models import VehicleCompany, VehicleModel


class VehicleRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_companies(self):
        statement = select(VehicleCompany)
        result = self.db.execute(statement)

        return result.scalars().all()

    def get_models_by_company(self, company: str):
        statement = (
            select(VehicleModel)
            .join(VehicleCompany)
            .where(VehicleCompany.name.ilike(company))
        )

        result = self.db.execute(statement)

        return result.scalars().all()