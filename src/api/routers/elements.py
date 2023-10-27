"""Elements Router FastAPI"""

# FastAPI
from fastapi import APIRouter

# Elements
# from src.modules.element.application import IntersectElementsCommand, list_elements_query

router = APIRouter(prefix='/elements', tags=['elements'])

@router.post('/intersection')
def elements_intersection(
    name: str,
    status: int,
):
    return {'body': (name, status)}
