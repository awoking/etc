from fastapi import FastAPI
from typing import Union

app = FastAPI()

fake_items_db = [{"item_name": "Foo"},
                 {"item_name": "Bar"},
                 {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int, limit: int):
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    return item