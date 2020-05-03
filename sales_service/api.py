from typing import List

from fastapi import APIRouter, HTTPException, status

from .db import session
from .models import Order, Seller
from .schemas import OrderCreate, OrderDetail, SellerAuth, SellerCreate, SellerDetail

router = APIRouter()


@router.post("/sellers/", status_code=status.HTTP_201_CREATED, response_model=SellerDetail)
async def sellers_create(seller: SellerCreate):
    if session.query(Seller).filter(Seller.email == seller.email).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="This email is already registered")

    if session.query(Seller).filter(Seller.cpf == seller.cpf).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="This CPF is already registered")

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


@router.post("/orders/", status_code=status.HTTP_201_CREATED, response_model=OrderDetail)
async def orders_create(order: OrderCreate):
    order_instance = Order(**order.to_db())
    session.add(order_instance)
    session.commit()
    session.refresh(order_instance)

    return order_instance


@router.get("/orders/", status_code=status.HTTP_200_OK, response_model=List[OrderDetail])
async def orders_list():
    return session.query(Order).all()
