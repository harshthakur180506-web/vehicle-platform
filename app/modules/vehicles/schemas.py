from pydantic import BaseModel


class CompanyResponse(BaseModel):
    name: str


class ModelResponse(BaseModel):
    name: str