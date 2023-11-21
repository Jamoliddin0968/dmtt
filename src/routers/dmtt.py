from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.dependencies import get_admin
from src.schemas.dmtt import DmttBase, DmttCreate, DmttUpdate
from src.services.dmtt import DmttService

router = APIRouter(prefix="/dmtt", tags=["Dmtt"])


@router.get('/all', response_model=List[DmttBase])
def get_all_dmtt(db: Session = Depends(get_db), user=Depends(get_admin)):
    return DmttService.get_all_dmtt(db=db)


@router.get('/{stir}', response_model=DmttBase)
def get_all_dmtt(stir: int, db: Session = Depends(get_db), user=Depends(get_admin)):
    return DmttService.get_dmtt_by_stir(stir=stir, db=db)


@router.post("/create")
async def create(data: DmttCreate, db: Session = Depends(get_db), user=Depends(get_admin)):
    if DmttService.check_existing_stir(data.stir, db):
        raise HTTPException(
            status_code=422, detail="Bu STIR li foydalanuvchi allaqachon mavjud")
    new_dmtt = await DmttService.create_dmtt(data=data, db=db)
    return new_dmtt


@router.put("/update/{stir}")
async def update_dmtt(stir: str, data: DmttUpdate, db: Session = Depends(get_db), user=Depends(get_admin)):
    instance = DmttService.get_dmtt_by_stir(stir, db)
    if instance is None:
        raise HTTPException(status_code=404, detail="dmtt not found")
    updated_instance = await DmttService.update_dmtt(stir=stir, data=data, db=db)
    return updated_instance


@router.delete("/delete/{stir}")
def delete_dmtt(stir: int, db: Session = Depends(get_db), user=Depends(get_admin)):
    instance = DmttService.get_dmtt_by_stir(stir, db)
    if instance is None:
        raise HTTPException(status_code=404, detail="dmtt not found")
    DmttService.delete_dmtt(instance=instance, db=db)
    return {"detail": "delete"}
