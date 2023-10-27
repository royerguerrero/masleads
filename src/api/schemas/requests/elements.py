"""Elements Request Schemas"""

# FastAPI
from pydantic import BaseModel


class ElementIntersectionSchema(BaseModel):
    name: str
    status: int
