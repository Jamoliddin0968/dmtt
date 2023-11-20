from fastapi import FastAPI

from src.database import get_db
from src.routers.dmtt import router as dmmt_router
from src.routers.organization import router as organization_router

app = FastAPI()


@app.get("/")
async def getHello():
    return {"Hello": "World"}

app.include_router(organization_router)
app.include_router(dmmt_router)
