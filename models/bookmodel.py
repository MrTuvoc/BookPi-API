from pydantic import BaseModel
from datetime import date
class Book(BaseModel):
    name: str
    description: str
    publishing_date: date