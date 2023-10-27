"""Element Status Enum"""

# Built-ins
from enum import Enum


class ElementStatusEnum(Enum):
    PENDING = 20
    PROCESSING = 60
    FAILED = 80
    PROCESSED = 100
