
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
    return SeasonProductService.create_season_product(db=db, data=data)


@router.get("/{season}", response_model=List[SeasonProductInfo])
def read_season_product(season: int, db: Session = Depends(get_db)):
    db_season_product = SeasonProductService.get_products_by_season_id(
        db=db, season=season)
    return db_season_product


@router.delete("/{season_product_id}")
def delete_season_product(season_product_id: int, db: Session = Depends(get_db)):
    return SeasonProductService.delete_season_product(
        db=db, season_product_id=season_product_id)
