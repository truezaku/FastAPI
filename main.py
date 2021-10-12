#FastAPI
from typing import Optional
from fastapi import FastAPI, Query, Path

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get('/validation/{path}')
async def validation(
        string: str = Query(None, min_length=2, max_length=5, regex=r'[a-c]+.'),
        integer: int = Query(..., gt=1, le=3),  # required
        alias_query: str = Query('default', alias='alias-query'),
        path: int = Path(10)):

    return {"string": string, "integer": integer, "alias-query": alias_query, "path": path}

#@app.get("/recommend")
