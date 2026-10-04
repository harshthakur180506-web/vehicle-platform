from app.database.base import Base
from app.database.connection import engine

from app.database.models import VehicleCompany, VehicleModel


print("Starting table creation...")

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")