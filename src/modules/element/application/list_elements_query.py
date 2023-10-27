"""List Elements Query"""

# Shared
from src.modules.shared.application import Query, QueryResponse, AbstractUnitOfWork

# Build-ins
from dataclasses import dataclass


@dataclass
class ElementQuery(Query):
    id: int
    name: str
    status: int


def list_elements_query(
    uow: AbstractUnitOfWork,
    status: int,
) -> QueryResponse:
    return QueryResponse(dto=[ElementQuery(id=1, name='test', status=status)])
