from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class VehicleCompany(Base):

    __tablename__ = "vehicle_companies"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    models: Mapped[list["VehicleModel"]] = relationship(
        back_populates="company"
    )