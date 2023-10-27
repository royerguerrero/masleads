"""Element Status Must Exits Business Rule"""

# Shared
from src.modules.shared.domain import BusinessRule

# Local
from src.modules.element.domain import ElementStatusEnum

# Build-ins
from dataclasses import dataclass


@dataclass
class ElementStatusMustExits(BusinessRule):
    status: int

    def is_broken(self) -> bool:
        return self.status not in [status.value for status in ElementStatusEnum]
