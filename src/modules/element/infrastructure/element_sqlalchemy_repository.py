# Shared
from src.modules.shared.infrastructure import SQLAlchemyRepository

# Local
from src.modules.element.domain import ElementRepository
from src.modules.element.infrastructure import ElementSQLAlchemyDataMapper


class ElementSQLAlchemyRepository(SQLAlchemyRepository, ElementRepository):
    data_mapper = ElementSQLAlchemyDataMapper
