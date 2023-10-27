"""Element Aggregate Root"""

# Shared
from src.modules.shared.domain import AggregateRoot

# Local
from src.modules.element.domain import ElementId, ElementStatusEnum
from src.modules.element.domain.business_rules import ElementStatusMustExits


class Element(AggregateRoot):
    def __init__(
        self,
        id: int,
        retries: int,
        status: int,
        name: str
    ) -> None:
        self.id = id
        self.retries = retries
        self.status = status
        self.name = name

    @property
    def id(self) -> int:
        return self._id.value

    @id.setter
    def id(self, value: int) -> None:
        self._id = ElementId(value=value)

    @property
    def retries(self) -> int:
        return self._retries

    @retries.setter
    def retries(self, value: int) -> None:
        self._retries = value

    @property
    def status(self) -> int:
        return self._status.value

    @status.setter
    def status(self, value: int) -> None:
        self.check_rule(ElementStatusMustExits(value))
        self._status = ElementStatusEnum(value)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value
