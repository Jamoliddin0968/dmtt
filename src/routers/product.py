
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.schemas.product import ProductCreate, ProductInfo, ProductUpdate
from src.services.product import ProductService

router = APIRouter(prefix='/product', tags=["product"])


@router.post("/create", response_model=ProductInfo)
def create_product(data: ProductCreate, db: Session = Depends(get_db)):
    return ProductService.create_product(db=db, product_data=data)


@router.get("/all", response_model=list[ProductInfo])
def read_products(db: Session = Depends(get_db)):
    return ProductService.get_products(db=db)


@router.get("/{product_id}", response_model=ProductInfo)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = ProductService.get_product_by_id(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.put("/update/{product_id}", response_model=ProductInfo)
def update_product(product_id: int, data: ProductUpdate, db: Session = Depends(get_db)):
    db_product = ProductService.get_product_by_id(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return ProductService.update_product(db=db, product_id=product_id, product_data=data)


@router.delete("/delete/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = ProductService.get_product_by_id(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    ProductService.delete_product(db=db, product_id=product_id)
    return {"message": "Product deleted"}
