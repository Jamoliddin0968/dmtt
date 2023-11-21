from fastapi import FastAPI
from fastapi.responses import UJSONResponse

from src.routers.auth import router as auth_router
from src.routers.dmtt import router as dmmt_router
from src.routers.organization import router as organization_router
from src.routers.user import router as user_router

app = FastAPI()


@app.get("/")
def getHello():
    return UJSONResponse(content={"Hello": "World"})


app.include_router(organization_router)
app.include_router(dmmt_router)
app.include_router(user_router)
app.include_router(auth_router)
