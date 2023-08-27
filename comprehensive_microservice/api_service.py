from fastapi import FastAPI, HTTPException

from .coder import DataCoder, DataModel, Storage

app = FastAPI()
data_coder = DataCoder(Storage())


@app.post("/save")
async def save_data(data: DataModel) -> dict[str, str]:
    key = data_coder.save(data)
    return {"key": key}


@app.get("/get/{item_id}")
async def get_data(item_id: str) -> DataModel:
    try:
        return data_coder.get(item_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Path not found")
