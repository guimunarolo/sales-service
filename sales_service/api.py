import uuid

from fastapi import APIRouter, status

from .db import database, sellers_orm
from .models import SellerCreate, SellerDetail

router = APIRouter()


@router.post("/sellers/", status_code=status.HTTP_201_CREATED, response_model=SellerDetail)
async def seller_create(seller: SellerCreate):
    _id = str(uuid.uuid4())
    query = sellers_orm.insert().values(id=_id, **seller.dict())
    await database.execute(query)

    return {"id": _id, **seller.dict()}
