from coder import DataCoder, DataModel
from fastapi import FastAPI

app = FastAPI()
data_coder = DataCoder()


@app.post("/save")
async def save_data(data: DataModel) -> str:
    return data_coder.save(data)


@app.get("/get")
async def get_data(key: str) -> DataModel:
    return data_coder.get(key)
