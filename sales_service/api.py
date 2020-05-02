from typing import List

from fastapi import APIRouter, HTTPException, status

from .db import session
from .models import Seller
from .schemas import SellerAuth, SellerCreate, SellerDetail

router = APIRouter()


@router.post("/sellers/", status_code=status.HTTP_201_CREATED, response_model=SellerDetail)
async def sellers_create(seller: SellerCreate):
    seller_instance = Seller(**seller.dict())

    session.add(seller_instance)
    session.commit()
    session.refresh(seller_instance)

    return seller_instance


@router.get("/sellers/", status_code=status.HTTP_200_OK, response_model=List[SellerDetail])
async def sellers_list():
    return session.query(Seller).all()


@router.post("/sellers/authentication/", status_code=status.HTTP_200_OK, response_model=SellerDetail)
async def sellers_authentication(auth: SellerAuth):
    seller = session.query(Seller).filter(Seller.email == auth.email).first()
    if seller and seller.password == auth.password:
        return seller

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
