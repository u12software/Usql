from typing import Dict, Any

from usql.models.metamodel import MetaModel
from usql.models.manager import (
    ModelManager
)


class Model(
    metaclass=MetaModel
):

    _fields: Dict[str, Any] = {}

    def __init__(self, **kwargs):

        for field_name in self._fields:

            setattr(
                self,
                field_name,
                kwargs.get(field_name)
            )

    def to_dict(self):

        data = {}

        for field_name in self._fields:

            data[field_name] = getattr(
                self,
                field_name
            )

        return data
    
    @classmethod
    def create(cls, **kwargs):

        return ModelManager.create(
            cls,
            **kwargs
        )


    @classmethod
    def all(cls):

        return ModelManager.all(
            cls
        )
    
    @classmethod
    def get(cls, **filters):

        return ModelManager.get(
            cls,
            **filters
        )
    
    @classmethod
    def filter(cls, **filters):

        return ModelManager.filter(
            cls,
            **filters
        )
    
    @classmethod
    def count(cls):

        return ModelManager.count(
            cls
        )