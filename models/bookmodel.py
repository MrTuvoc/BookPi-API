from pydantic import BaseModel
from datetime import date
from uuid import UUID
class Book(BaseModel):
    name: str
    description: str
    publishing_date: date