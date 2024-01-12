from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.schemas.dmtt import DmttCreate, DmttInfo, DmttUpdate, PersonCreate, PersonUpdate
from src.services.dmtt import DmttService, DmttPersonService

router = APIRouter(prefix="/dmtts", tags=["Dmtt"])


@router.get('', response_model=List[DmttInfo])
def get_all_dmtt(db: Session = Depends(get_db)):
    return DmttService.get_all_dmtt(db=db)


@router.get('/{id}', response_model=DmttInfo)
def get_dmtt(id: int, db: Session = Depends(get_db)):
    return DmttService.get_dmtt_by_id(id=id, db=db)


@router.post("/")
async def create(data: DmttCreate, db: Session = Depends(get_db)):
    return await DmttService.create_dmtt(data=data, db=db)


@router.put("/{id}")
async def update_dmtt(id: int, data: DmttUpdate, db: Session = Depends(get_db)):
    return await DmttService.update_dmtt(id=id, data=data, db=db)


@router.delete("/{id}")
def delete_dmtt(id: int, db: Session = Depends(get_db)):
    return DmttService.delete_dmtt(id=id, db=db)


@router.post("/persons/")
def create_person_api(person: PersonCreate, db: Session = Depends(get_db)):
    return DmttPersonService.create_person(db, person)


@router.get("/persons/{person_id}")
def read_person(person_id: int, db: Session = Depends(get_db)):
    db_person = DmttPersonService.get_person(db, person_id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person


@router.get("/persons/")
def read_all_persons(db: Session = Depends(get_db)):
    return DmttPersonService.get_all_persons(db)


@router.put("/persons/{person_id}")
def update_person_api(person_id: int, updates: PersonUpdate, db: Session = Depends(get_db)):
    db_person = DmttPersonService.get_person(db, person_id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return DmttPersonService.update_person(db, person_id, updates)


@router.delete("/persons/{person_id}", response_model=dict)
def delete_person_api(person_id: int, db: Session = Depends(get_db)):
    db_person = DmttPersonService.get_person(db, person_id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return DmttPersonService.delete_person(db, person_id)
