from fastapi import FastAPI

from .api import router as api_router
from .db import database, engine, metadata

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


metadata.create_all(engine)
app.include_router(api_router)
