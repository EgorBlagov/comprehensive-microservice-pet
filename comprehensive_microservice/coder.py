from random import randint
from typing import Any

from pydantic import BaseModel


class DataModel(BaseModel):
    title: str
    text: str


class Storage(dict[str, Any]):
    pass


class DataCoder:
    def __init__(self, storage: Storage):
        self.storage = storage

    def save(self, data: DataModel) -> str:
        while True:
            key = str(randint(1, 100000))
            if key not in self.storage:
                break
        self.storage[key] = data.model_dump()
        return key

    def get(self, code: str) -> DataModel:
        return DataModel.model_validate(self.storage[code])
