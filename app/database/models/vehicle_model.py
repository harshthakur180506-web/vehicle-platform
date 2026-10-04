from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

class VehicleModel(Base):
    __tablename__ = "vehicle_models"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
         )

    company_id: Mapped[int] = mapped_column(
        ForeignKey("vehicle_companies.id"),
        nullable=False
    )

    company: Mapped["VehicleCompany"] = relationship(
        back_populates="models"
    )