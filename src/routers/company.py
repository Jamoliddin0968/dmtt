from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.dependencies import get_admin
from src.schemas.company import CompanyCreate, CompanyInfo, CompanyUpdate
from src.services.company import CompanyService as service

router = APIRouter(prefix="/companies", tags=["Firma"])


@router.get("/search/{q}", response_model=List[CompanyInfo])
def search_company(q: str):
    return service.search_company(q)


@router.get("/", response_model=List[CompanyInfo])
def get_all_company(db: Session = Depends(get_db), user=Depends(get_admin)):
    return service.get_all_companys(db)


@router.get("/{id}", response_model=CompanyInfo)
def get_company(id: int, db: Session = Depends(get_db), user=Depends(get_admin)):
    return service.get_company_by_id(id=id, db=db)


@router.post("/", response_model=CompanyInfo)
async def create(data: CompanyCreate, db: Session = Depends(get_db), user=Depends(get_admin)):
    return await service.create_company(data=data, db=db)


@router.put("/{id}", response_model=CompanyInfo)
async def update_company(id: int, data: CompanyUpdate, db: Session = Depends(get_db), user=Depends(get_admin)):
    return await service.update_company(id=id, data=data, db=db)


@router.delete("/{id}")
def delete_company(id: int, db: Session = Depends(get_db), user=Depends(get_admin)):
    return service.delete_company(id=id, db=db)
