"""Abstract Unit Of Work"""

# Build-ins
from abc import ABC, abstractclassmethod

# Abstract Repositories
from src.modules.element.domain import ElementRepository


class AbstractUnitOfWork(ABC):
    """Abstract Unit Of Work"""
    # Set here the abstract repositories
    element_repository: ElementRepository

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @abstractclassmethod
    def commit(self):
        raise NotImplementedError

    @abstractclassmethod
    def rollback(self):
        raise NotImplementedError
