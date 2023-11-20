from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.responses import UJSONResponse
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.dmtt import Dmtt
# from src.models.dmtt import dmtt
from src.schemas.dmtt import DmttBase, DmttCreate, DmttInfo, DmttUpdate
from src.services.dmtt import createDmtt, deleteDmtt, getAllDmtt, updateDmtt

router = APIRouter(prefix="/dmtt", tags=["Dmtt",])


@router.get('/all', response_model=List[DmttBase])
def get_all_dmtt(db: Session = Depends(get_db)):
    return getAllDmtt(db=db)


@router.post("/create")
async def create(data: DmttCreate, db: Session = Depends(get_db)):
    if db.query(Dmtt).filter(Dmtt.stir == data.stir).first():
        raise HTTPException(
            status_code=422, detail="Bu STIR li foydalanuvchi allaqachon mavjud")
    new_dmtt = await createDmtt(data=data, db=db)
    return new_dmtt


@router.put("/update/{stir}")
async def update_dmtt(stir: str, data: DmttUpdate, db: Session = Depends(get_db)):
    instance = db.query(Dmtt).filter(
        Dmtt.stir == stir).first()

    if instance is None:
        raise HTTPException(status_code=404, detail="dmtt not found")
    instance = await updateDmtt(stir=stir, data=data, db=db)
    return instance


@router.delete("delete/{stir}/")
def delete_dmtt(stir: int, db: Session = Depends(get_db)):
    instance = db.query(Dmtt).filter(
        Dmtt.stir == stir).first()

    if instance is None:
        raise HTTPException(status_code=404, detail="dmtt not found")
    _ = deleteDmtt(instance, db=db)
    return UJSONResponse(content={"detail": "delete"}, status_code=200)
