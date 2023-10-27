"""FastAPI Dependencies"""

# Shared
from src.modules.shared.infrastructure import Bootstrap

# Registries
from src.modules.element.infrastructure import ElementRegistry

bootstrap = Bootstrap(registries=[ElementRegistry])
