
from fastapi import APIRouter

router = APIRouter(prefix='connection')


@router.get("/all")
def get_all_connection():
    return {"hello": "world"}

