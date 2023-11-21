from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import UJSONResponse
from sqlalchemy.orm import Session

from src.database import get_db
# from src.models.organization import Organization
from src.schemas.organization import (CompanyInfo, OrganizationCreate,
                                      OrganizationUpdate)
from src.services.organization import OrganizationService as service

router = APIRouter(prefix="/organization", tags=["Firma"])


@router.get("/search/{q}", response_model=List[CompanyInfo])
def search_organization(q: str):
    res = service.search_organization(q)
    return res


@router.get("/all", response_model=List[CompanyInfo])
def get_all_organizations(db: Session = Depends(get_db)):
    return service.get_all_organizations(db)


@router.post("/create", response_model=CompanyInfo)
async def create(data: OrganizationCreate, db: Session = Depends(get_db)):
    if service.get_organization_by_stir(data.stir, db):
        raise HTTPException(
            status_code=422, detail="Bu STIR li foydalanuvchi allaqachon mavjud"
        )
    new_organization = await service.create_organization(data=data, db=db)
    return new_organization


@router.put("/update/{stir}", response_model=CompanyInfo)
async def update_organization(stir: int, data: OrganizationUpdate, db: Session = Depends(get_db)):
    instance = service.get_organization_by_stir(stir, db)

    if not instance:
        raise HTTPException(status_code=404, detail="Organization not found")
    updated_instance = await service.update_organization(instance=instance, data=data, db=db)
    return updated_instance


@router.delete("/delete/{stir}/")
def delete_organization(stir: int, db: Session = Depends(get_db)):
    instance = service.get_organization_by_stir(stir, db)

    if not instance:
        raise HTTPException(status_code=404, detail="Organization not found")
    service.delete_organization(instance, db)
    return UJSONResponse(content={"detail": "delete"}, status_code=200)
