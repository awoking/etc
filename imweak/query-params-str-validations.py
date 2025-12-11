from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()


@app.get("/items/")
async def read_items(
    q:Annotated[str | None, Query(
        default=None,
        min_length=3, 
        max_length=50, 
        pattern="^fixedquery$", 
        title="Query String", 
        description="A query string that must be 'fixedquery'", 
        deprecated=True,
        alias="item-query" 
    )] = "fixedquery",
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# クエリパラメーターのバリデーション
# いろいろできるよ
# Unionの上位互換がAnnotatedであるよって話