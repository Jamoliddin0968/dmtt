from sqlalchemy.orm import Session

from src.models.season_product import SeasonProduct


class SeasonProductService:
    @staticmethod
    def create_season_product(db: Session, data) -> SeasonProduct:
        new_season_product = SeasonProduct(
            data.model_dump())
        db.add(new_season_product)
        db.commit()
        db.refresh(new_season_product)
        return new_season_product

    @staticmethod
    def get_season_product_by_id(db: Session, season_product_id: int) -> SeasonProduct:
        return db.query(SeasonProduct).filter(SeasonProduct.id == season_product_id).first()

    @staticmethod
    def update_season_product(db: Session, season_product_id: int, season: int) -> SeasonProduct:
        db_season_product = SeasonProductService.get_season_product_by_id(
            db, season_product_id)
        if db_season_product:
            db_season_product.season = season
            db.commit()
            db.refresh(db_season_product)
            return db_season_product

    @staticmethod
    def delete_season_product(db: Session, season_product_id: int) -> bool:
        db_season_product = SeasonProductService.get_season_product_by_id(
            db, season_product_id)
        if db_season_product:
            db.delete(db_season_product)
            db.commit()
            return True
        return False

    @staticmethod
    def get_products_by_season_id(db: Session, season: int) -> SeasonProduct:
        return db.query(SeasonProduct).filter(SeasonProduct.season == season).all()
