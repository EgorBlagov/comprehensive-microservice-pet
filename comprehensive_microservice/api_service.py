from fastapi import FastAPI

from .coder import DataCoder, DataModel, Storage

app = FastAPI()
data_coder = DataCoder(Storage())


@app.post("/save")
async def save_data(data: DataModel) -> str:
    return data_coder.save(data)


@app.get("/get")
async def get_data(key: str) -> DataModel:
    return data_coder.get(key)
