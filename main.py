from fastapi import FastAPI
from fastapi.responses import UJSONResponse

from src.routers.base import router as base_router

app = FastAPI()

app.include_router(base_router)


@app.get("/")
def getHello():
    return UJSONResponse(content={"Hello": "World"})
