from fastapi import HTTPException
from sqlalchemy import select, text
from sqlalchemy.orm import Session

from src.models.product import Product
from src.schemas.product import ProductCreate


class ProductService:
    def create_product(db, product_data: ProductCreate):
        db_product = Product(**product_data.model_dump())
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product

    def get_products(db):
        result = db.execute(text("select * from products")).fetchall()
        return result

    def get_product_by_id(db, product_id):
        product = db.query(Product).filter(Product.id == product_id).first()
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        return product

    def update_product(db, product_id, product_data):
        db_product = ProductService.get_product_by_id(
            db=db, product_id=product_id)
        product_data = product_data.model_dump()
        for key, value in product_data.items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
        return db_product

    def delete_product(db, product_id):
        db_product = ProductService.get_product_by_id(
            db=db, product_id=product_id)
        db.delete(db_product)
        db.commit()
        return {"message": "Product deleted"}

    @staticmethod
    def get_winter_products(db: Session):
        return db.query(Product).filter(Product.winter == True).all()

    @staticmethod
    def get_summer_products(db: Session):
        return db.query(Product).filter(Product.summer == True).all()

    @staticmethod
    def get_spring_products(db: Session):
        return db.query(Product).filter(Product.spring == True).all()

    @staticmethod
    def get_autumn_products(db: Session):
        return db.query(Product).filter(Product.autumn == True).all()
