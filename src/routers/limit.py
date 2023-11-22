
from fastapi import APIRouter

router = APIRouter(prefix='limit')


@router.get("/all")
def get_all_limit():
    return {"hello": "world"}

