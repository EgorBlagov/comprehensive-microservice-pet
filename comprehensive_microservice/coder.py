from pydantic import BaseModel
from random import randint


class DataModel(BaseModel):
    title: str
    text: str


class Storage(dict):
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
