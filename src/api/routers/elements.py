"""Elements Router FastAPI"""

# FastAPI
from fastapi import APIRouter, Depends, HTTPException
from src.api.dependencies import bootstrap

# Shared
from src.modules.shared.infrastructure import Bootstrap

# Elements
from src.modules.element.application import IntersectElementsCommand, list_elements_query

# Schemas
from src.api.schemas.requests.elements import ElementIntersectionSchema
from src.api.schemas.responses.elements import ElementResponseSchema


router = APIRouter(prefix='/elements', tags=['elements'])


@router.post('/intersection')
def elements_intersection(
    name: str,
    status: int,
    bootstrap: Bootstrap = Depends(bootstrap)
) -> list[ElementResponseSchema]:
    command = IntersectElementsCommand(name=name, status=status)

    response = bootstrap.bus.handle(command)
    if response.command.has_errors:
        raise HTTPException(status_code=400, detail=response.command.errors)

    query_response = list_elements_query(
        uow=bootstrap.uow,
        status=status,
    )
    if query_response.has_errors:
        raise HTTPException(status_code=404, detail=query_response.errors)

    return [
        ElementIntersectionSchema(**element_query.as_dict())
        for element_query in query_response.dto
    ]
