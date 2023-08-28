from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException

from .coder import DataCoder, DataModel, Storage
from .utils import single_call

app = FastAPI()


@single_call
def get_storage() -> Storage:
    return Storage()


@single_call
def get_data_coder(storage: Annotated[Storage, Depends(get_storage)]) -> DataCoder:
    return DataCoder(storage)


@app.post("/save")
async def save_data(
    data: DataModel, dc: Annotated[DataCoder, Depends(get_data_coder)]
) -> dict[str, str]:
    key = dc.save(data)
    return {"key": key}


@app.get("/get/{item_id}")
async def get_data(
    item_id: str, dc: Annotated[DataCoder, Depends(get_data_coder)]
) -> DataModel:
    try:
        return dc.get(item_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Path not found")
