# Shared
from src.modules.shared.infrastructure import SQLAlchemyDataMapper

# Local
from src.modules.element.domain import Element
from src.modules.element.infrastructure import ElementSQLAlchemyModel


class ElementSQLAlchemyDataMapper(SQLAlchemyDataMapper):
    MAPPING = {
        Element.id: ElementSQLAlchemyModel.id,
        Element.retries: ElementSQLAlchemyModel.retries,
        Element.status: ElementSQLAlchemyModel.status,
        Element.name: ElementSQLAlchemyModel.name,
    }
