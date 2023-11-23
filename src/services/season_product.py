from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.models.season_product import SeasonProduct
from src.services.product import ProductService


class SeasonProductService:
    @staticmethod
    def create_season_product(db: Session, data) -> SeasonProduct:
        ProductService.get_product_by_id(db=db, product_id=data.product_id)
        new_season_product = SeasonProduct(
            **data.model_dump()
        )
        db.add(new_season_product)
        db.commit()
        db.refresh(new_season_product)
        return new_season_product

    @staticmethod
    def get_season_product_by_id(db: Session, season_product_id: int) -> SeasonProduct:
        season_product = db.query(SeasonProduct).filter(
            SeasonProduct.id == season_product_id).first()
        if not season_product:
            raise HTTPException(
                status_code=404,
                detail="Bunday idli product mavjud emas"
            )
        return season_product

    @staticmethod
    def update_season_product(db: Session, season_product_id: int, season: int) -> SeasonProduct:
        db_season_product = SeasonProductService.get_season_product_by_id(
            db, season_product_id)
        db_season_product.season = season
        db.commit()
        db.refresh(db_season_product)
        return db_season_product

    @staticmethod
    def delete_season_product(db: Session, season_product_id: int) -> bool:
        season_product = SeasonProductService.get_season_product_by_id(
            db, season_product_id)
        db.delete(season_product)
        db.commit()
        return {"message": "Season Product deleted successfully"}

    @staticmethod
    def get_products_by_season_id(db: Session, season: int) -> SeasonProduct:
        return db.query(SeasonProduct).filter(SeasonProduct.season == season).all()
