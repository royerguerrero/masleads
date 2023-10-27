"""Elements Response Schemas"""

# FastAPI
from pydantic import BaseModel


class ElementResponseSchema(BaseModel):
    id: int
    name: str
    status: int
