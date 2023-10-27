"""Element SQLAlchemy Model"""

# Shared
from src.modules.shared.infrastructure import Base

# SQLAlchemy
from sqlalchemy import Column, Integer, String


class ElementSQLAlchemyModel(Base):
    __tablename__ = 'ElementsToProcess'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_bulk = Column(Integer, nullable=False)
    retries = Column(Integer)
    status = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
