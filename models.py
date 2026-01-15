# models.py
from pydantic import BaseModel

class Student(BaseModel):
    id: str
    name: str
    cgpa: float

class UpdateStudent(BaseModel):
    name: str | None = None
    cgpa: float | None = None