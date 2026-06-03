from typing import Type

class ModelRegistry:

    _models: dict[str, Type] = {}

    @classmethod
    def register(cls, model):

        cls._models[model.__name__] = model

    @classmethod
    def get(cls, name):

        return cls._models.get(name)

    @classmethod
    def all(cls):

        return cls._models