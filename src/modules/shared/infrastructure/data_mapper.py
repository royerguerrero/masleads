"""Data Mapper Shared"""

# Build-ins
from abc import ABC, abstractmethod

# Local
from src.modules.shared.domain import Entity
from src.modules.shared.infrastructure import Base

# Build-ins
from typing import Type, List


class DataMapper(ABC):
    @abstractmethod
    def models_to_entity(self, instances: List[Type[Base]]) -> Type[Entity]:
        """Serialize models to into Entity"""
        raise NotImplementedError

    @abstractmethod
    def entity_to_models(self, entity: Type[Entity]) -> List[Type[Base]]:
        """Serialize entity into models"""
        raise NotImplementedError
