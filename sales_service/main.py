from fastapi import FastAPI

from .api import router as api_router
from .db import Base, engine

app = FastAPI()


@app.on_event("startup")
async def startup():
    Base.metadata.create_all(engine)


app.include_router(api_router)
