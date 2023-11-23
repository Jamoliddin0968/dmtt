from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import UJSONResponse
from sqlalchemy.orm import Session

from src.database import get_db
from src.dependencies import get_admin
from src.schemas.company import CompanyCreate, CompanyInfo, CompanyUpdate
from src.services.company import CompanyService as service

router = APIRouter(prefix="/company", tags=["Firma"])


@router.get("/search/{q}", response_model=List[CompanyInfo])
def search_company(q: str):
    return service.search_company(q)


@router.get("/all", response_model=List[CompanyInfo])
def get_all_company(db: Session = Depends(get_db), user=Depends(get_admin)):
    return service.get_all_companys(db)


@router.get("/{stir}", response_model=CompanyInfo)
def get_company(stir: str, db: Session = Depends(get_db), user=Depends(get_admin)):
    return service.get_company_by_stir(stir=stir, db=db)


@router.post("/create", response_model=CompanyInfo)
async def create(data: CompanyCreate, db: Session = Depends(get_db), user=Depends(get_admin)):
    return await service.create_company(data=data, db=db)


@router.put("/update/{stir}", response_model=CompanyInfo)
async def update_company(stir: str, data: CompanyUpdate, db: Session = Depends(get_db), user=Depends(get_admin)):
    return await service.update_company(stir=stir, data=data, db=db)


@router.delete("/delete/{stir}/")
def delete_company(stir: int, db: Session = Depends(get_db), user=Depends(get_admin)):   
    return service.delete_company(stir=stir, db)
