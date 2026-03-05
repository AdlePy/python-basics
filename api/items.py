from fastapi import APIRouter


router = APIRouter(prefix="/items", tags=["items"])


@router.get("/")
async def get_items():
    return [
        {"item_id": 1},
        {"item_id": 2},
    ]


@router.post("/")
async def create_item(data: dict):
    return {"data": data}


@router.get("/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}
