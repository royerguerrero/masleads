"""ElementId value object"""

# Shared
from src.modules.shared.domain import ValueObject


class ElementId(ValueObject):
    def __init__(self, value: int):
        self.value = value
