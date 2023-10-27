"""Element Abstract Repository"""

# Shared
from src.modules.shared.domain import AbstractRepository

# Local
from src.modules.element.domain import Element


class ElementRepository(AbstractRepository):
    entity = Element
