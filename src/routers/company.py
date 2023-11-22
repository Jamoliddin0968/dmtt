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
    res = service.search_company(q)
    return res


@router.get("/all", response_model=List[CompanyInfo])
def get_all_company(db: Session = Depends(get_db), user=Depends(get_admin)):
    return service.get_all_companys(db)


@router.get("/{stir}", response_model=CompanyInfo)
def get_company(stir: str, db: Session = Depends(get_db), user=Depends(get_admin)):
    res = service.get_company_by_stir(stir=stir, db=db)
    if res:
        return res
    raise HTTPException(
        status_code=404, detail="not found"
    )


@router.post("/create", response_model=CompanyInfo)
async def create(data: CompanyCreate, db: Session = Depends(get_db), user=Depends(get_admin)):
    if service.get_company_by_stir(data.stir, db):
        raise HTTPException(
            status_code=422, detail="Bu STIR li foydalanuvchi allaqachon mavjud"
        )
    new_company = await service.create_company(data=data, db=db)
    return new_company


@router.put("/update/{stir}", response_model=CompanyInfo)
async def update_company(stir: int, data: CompanyUpdate, db: Session = Depends(get_db), user=Depends(get_admin)):
    instance = service.get_company_by_stir(stir, db)

    if not instance:
        raise HTTPException(status_code=404, detail="Company not found")
    updated_instance = await service.update_company(instance=instance, data=data, db=db)
    return updated_instance


@router.delete("/delete/{stir}/")
def delete_company(stir: int, db: Session = Depends(get_db), user=Depends(get_admin)):
    instance = service.get_company_by_stir(stir, db)

    if not instance:
        raise HTTPException(status_code=404, detail="Company not found")
    service.delete_company(instance, db)
    return UJSONResponse(content={"detail": "delete"}, status_code=200)
