from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.dependencies import get_admin
from src.schemas.dmtt import DmttCreate, DmttInfo, DmttUpdate
from src.services.dmtt import DmttService

router = APIRouter(prefix="/dmtt", tags=["Dmtt"])


@router.get('/all', response_model=List[DmttInfo])
def get_all_dmtt(db: Session = Depends(get_db), user=Depends(get_admin)):
    return DmttService.get_all_dmtt(db=db)


@router.get('/{id}', response_model=DmttInfo)
def get_all_dmtt(id: int, db: Session = Depends(get_db), user=Depends(get_admin)):
    return DmttService.get_dmtt_by_id(id=id, db=db)


@router.post("/create")
async def create(data: DmttCreate, db: Session = Depends(get_db)):
    return await DmttService.create_dmtt(data=data, db=db)


@router.put("/update/{id}")
async def update_dmtt(id: str, data: DmttUpdate, db: Session = Depends(get_db), user=Depends(get_admin)):
    return await DmttService.update_dmtt(id=id, data=data, db=db)


@router.delete("/delete/{id}")
def delete_dmtt(id: int, db: Session = Depends(get_db), user=Depends(get_admin)):
    return DmttService.delete_dmtt(id=id, db=db)
