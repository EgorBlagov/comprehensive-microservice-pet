from pydantic import BaseModel
from random import randint


class DataModel(BaseModel):
    title: str
    text: str


class DataCoder:
    def __init__(self):
        self.storage = {}

    def save(self, data: DataModel) -> str:
        while True:
            new_id = str(randint(1, 100000))
            if new_id not in self.storage.keys():
                break
        self.storage[new_id] = (data.title, data.text)
        return new_id

    def get(self, code: str) -> DataModel:
        tuple_ = self.storage[code]
        data = DataModel(title=tuple_[0], text=tuple_[1])
        return data


# some_var = DataCoder()
# id = some_var.save(DataModel(title="gavno", text="shit"))
# print(id)
# print(some_var.get(id))
