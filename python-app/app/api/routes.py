from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def index():
    return {"message": "Hello, World!"}


@router.get("/items")
async def list_items():
    return {
        "items": [
            {"id": 1, "name": "Item One"},
            {"id": 2, "name": "Item Two"},
            {"id": 3, "name": "Item Three"},
        ]
    }


@router.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"id": item_id, "name": f"Item {item_id}"}
