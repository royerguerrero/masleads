"""SQlAlchemy Generic DataMapper"""

# Local
from src.modules.shared.domain import Entity
from src.modules.shared.infrastructure import DataMapper, Base

# Third-parties
from sqlalchemy.orm.attributes import InstrumentedAttribute

# Build-ins
from typing import Type, Dict, List


class SQLAlchemyDataMapper(DataMapper):
    MAPPING = Dict[property, InstrumentedAttribute]

    def _pre_instance_entity(self, entity_data: Dict, instances: List[Type[Base]]) -> Dict:
        return entity_data

    @classmethod
    def models_to_entity(cls, instances: List[Type[Base]]) -> Type[Entity]:
        entity_data = {}
        entity_class = None
        for entity_field, model_column in cls.MAPPING.items():
            if not isinstance(entity_field, property):
                continue

            entity_class_name = entity_field.fget.__qualname__.split('.')[0]
            entity_class_aux = entity_field.fget.__globals__[entity_class_name]

            if entity_class is not None and entity_class_aux != entity_class:
                raise Exception(
                    'The entity class must be the same for all fields'
                )

            entity_class = entity_class_aux

            for instance in instances:
                if model_column.class_ == instance.__class__:
                    model_column_value = getattr(
                        instance,
                        model_column.key,
                        None
                    )
                    entity_data[entity_field.fget.__name__] = model_column_value

        entity_data = cls._pre_instance_entity(
            self=cls,
            entity_data=entity_data,
            instances=instances,
        )
        return entity_class(**entity_data)

    def _entity_to_model(self, entity: Type[Entity], model: Type[Base]) -> Type[Base]:
        model_data = {}
        for entity_field, model_column in self.MAPPING.items():
            if model == model_column.class_:
                # Allows the default values in the SQLAlchemy data mappers
                entity_field_value = getattr(
                    entity,
                    entity_field.fget.__name__
                ) if isinstance(entity_field, property) else entity_field
                model_data[model_column.key] = entity_field_value

        return model(**model_data)

    def _pre_instance_model_models(self, models: Dict, entity: Type[Entity]) -> Dict:
        return models

    @classmethod
    def entity_to_models(cls, entity: Type[Entity]) -> List[Type[Base]]:
        models = {}
        for model_column in cls.MAPPING.values():
            model = models.get(model_column.class_.__name__, None)
            if model is None:
                models[model_column.class_.__name__] = cls._entity_to_model(
                    self=cls,
                    entity=entity,
                    model=model_column.class_
                )

        models = cls._pre_instance_model_models(
            self=cls,
            models=models,
            entity=entity,
        )
        return list(models.values())

    @classmethod
    @property
    def models(cls) -> List[Type[Base]]:
        return list(set(model_column.class_ for model_column in cls.MAPPING.values()))

    @classmethod
    @property
    def multiple_models(self) -> bool:
        return len(self.models) > 1
