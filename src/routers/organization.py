from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.responses import UJSONResponse
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.organization import Organization
# from src.models.organization import Organization
from src.schemas.organization import (CompanyInfo, OrganizationCreate,
                                      OrganizationUpdate)
from src.services.organization import (createOrganization, deleteOrganization,
                                       searchOrganization, updateOrganization)

router = APIRouter(prefix="/organization", tags=["Firma",])


@router.get("/search/{q}")
def search_organization(q: str) -> List[CompanyInfo]:
    res = searchOrganization(q)
    return res


@router.post("/create")
async def create(data: OrganizationCreate, db: Session = Depends(get_db)) -> CompanyInfo:
    if db.query(Organization).filter(Organization.stir == data.stir).first():
        raise HTTPException(
            status_code=422, detail="Bu STIR li foydalanuvchi allaqachon mavjud")
    new_organization = await createOrganization(data=data, db=db)
    return new_organization


@router.put("/update/{stir}")
async def update_organization(stir: int, data: OrganizationUpdate, db: Session = Depends(get_db)):
    instance = db.query(Organization).filter(
        Organization.stir == stir).first()

    if instance is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    instance = await updateOrganization(instance=instance, data=data, db=db)
    return instance


@router.delete("/delete/{stir}/")
def delete_organization(stir: int, db: Session = Depends(get_db)):
    instance = db.query(Organization).filter(
        Organization.stir == stir).first()

    if instance is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    _ = deleteOrganization(instance)
    return UJSONResponse(content={"detail": "delete"}, status_code=200)
