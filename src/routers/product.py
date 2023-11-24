
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.product import Product
from src.schemas.product import ProductCreate, ProductInfo, ProductUpdate
from src.services.product import ProductService

router = APIRouter(prefix='/product', tags=["product"])


@router.post("/create", response_model=ProductInfo)
def create_product(data: ProductCreate, db: Session = Depends(get_db)):
    return ProductService.create_product(db=db, product_data=data)


@router.get("/all", response_model=List[ProductInfo])
def read_products(db: Session = Depends(get_db)):
    return ProductService.get_products(db=db)


@router.get("/detail/{product_id}", response_model=ProductInfo)
def read_product(product_id: int, db: Session = Depends(get_db)):
    return ProductService.get_product_by_id(db=db, product_id=product_id)


@router.put("/update/{product_id}", response_model=ProductInfo)
def update_product(product_id: int, data: ProductUpdate, db: Session = Depends(get_db)):
    return ProductService.update_product(db=db, product_id=product_id, product_data=data)


@router.delete("/delete/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return ProductService.delete_product(db=db, product_id=product_id)


@router.get("/winter", response_model=List[ProductInfo])
def read_winter_products(db: Session = Depends(get_db)):
    return ProductService.get_winter_products(db=db)


@router.get("/summer", response_model=List[ProductInfo])
def read_summer_products(db: Session = Depends(get_db)):
    return ProductService.get_summer_products(db=db)


@router.get("/spring", response_model=List[ProductInfo])
def read_spring_products(db: Session = Depends(get_db)):
    return ProductService.get_spring_products(db=db)


@router.get("/autumn")
def read_autumn_products(db: Session = Depends(get_db)) -> List[ProductInfo]:
    return []
    return ProductService.get_autumn_products(db=db)
