
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.schemas.season_product import (SeasonProductCreate, SeasonProductInfo,
                                        SeasonProductUpdate)
from src.services.product import ProductService
from src.services.season_product import SeasonProductService

router = APIRouter(prefix="/season_products", tags=["Season Products"])


@router.post("/", response_model=SeasonProductInfo)
def create_season_product(data: SeasonProductCreate, db: Session = Depends(get_db)):
    if not 0 <= data.season <= 3:
        raise HTTPException(
            status_code=404,
            detail="Bunday season id mavjud emas"
        )
    if ProductService.get_product_by_id(db=db, product_id=data.product_id):
        return SeasonProductService.create_season_product(db=db, data=data)
    raise HTTPException(
        status_code=404,
        detail="Bunday idli product mavjud emas"
    )


@router.get("/{season}", response_model=List[SeasonProductInfo])
def read_season_product(season: int, db: Session = Depends(get_db)):
    db_season_product = SeasonProductService.get_products_by_season_id(
        db=db, season=season)
    return db_season_product


@router.delete("/{season_product_id}")
def delete_season_product(season_product_id: int, db: Session = Depends(get_db)):
    success = SeasonProductService.delete_season_product(
        db=db, season_product_id=season_product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Season Product not found")
    return {"message": "Season Product deleted successfully"}
