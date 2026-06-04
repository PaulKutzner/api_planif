from fastapi import FastAPI
from api.db import (engine,Base)
from api.routes import users
from api.models.user import User




app=FastAPI()


app.include_router(users.router)
Base.metadata.create_all(bind=engine)

