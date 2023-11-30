
from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from sqladmin import Admin, ModelView

from src.database import engine
from src.models.user import User
from chat import socket_app
from src.routers.base import router as base_router

app = FastAPI(debug=True)
app.include_router(base_router)
# fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
admin = Admin(app, engine)


class UserAdmin(ModelView, model=User):
    form_excluded_columns = ["password",]


admin.add_view(UserAdmin)

# mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm

# app.mount("/", socket_app)


@app.get("/")
def getHello():
    return UJSONResponse(content={"Hello": "World"})
