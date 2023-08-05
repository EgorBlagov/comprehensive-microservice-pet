from pydantic import BaseModel


class DataModel(BaseModel):
    title: str
    text: str


class DataCoder:
    def save(self, data: DataModel) -> str:
        raise NotImplementedError

    def get(self, code: str) -> DataModel:
        raise NotImplementedError
