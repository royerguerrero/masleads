# Shared
from src.modules.shared.infrastructure import Registry

# Local
from src.modules.element.application import (
    IntersectElementsCommand, intersect_elements
)

class ElementRegistry(Registry):
    command_handlers = {
        IntersectElementsCommand: intersect_elements
    }
    event_handlers = {}
