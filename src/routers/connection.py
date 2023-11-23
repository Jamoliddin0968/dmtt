from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.schemas.connection import ConnectionCreate, ConnectionInfo
from src.services.company import CompanyService
from src.services.connection import ConnectionService
from src.services.dmtt import DmttService
from src.services.product import ProductService

router = APIRouter(prefix='/connection', tags=["Connection"])


@router.post("/create", response_model=ConnectionInfo)
def create_connection(data: ConnectionCreate, db: Session = Depends(get_db)):
    return ConnectionService.create_connection(db=db, data=data)


@router.get("/{connection_id}", response_model=ConnectionInfo)
def read_connection(connection_id: int, db: Session = Depends(get_db)):
    db_connection = ConnectionService.get_connection_by_id(
        db=db, connection_id=connection_id)
    if db_connection is None:
        raise HTTPException(status_code=404, detail="Connection not found")
    return db_connection


@router.delete("/{connection_id}")
def delete_connection(connection_id: int, db: Session = Depends(get_db)):
    db_connection = ConnectionService.get_connection_by_id(
        db=db, connection_id=connection_id)
    if db_connection is None:
        raise HTTPException(status_code=404, detail="Connection not found")
    ConnectionService.delete_connection(db=db, connection_id=connection_id)
    return {"message": "Connection deleted"}


@router.get("/by_dmtt_id/{dmtt_id}", response_model=List[ConnectionInfo])
def get_connections_by_dmtt_id(dmtt_id: int, db: Session = Depends(get_db)):
    connections = ConnectionService.get_by_dmmt_id(db=db, dmtt_id=dmtt_id)
    return connections


@router.get("/by_product_id/{product_id}", response_model=List[ConnectionInfo])
def get_connections_by_product_id(product_id: int, db: Session = Depends(get_db)):
    connections = ConnectionService.get_by_product_id(
        db=db, product_id=product_id)
    return connections


@router.get("/by_company_id/{company_id}", response_model=List[ConnectionInfo])
def get_connections_by_company_id(company_id: int, db: Session = Depends(get_db)):
    return ConnectionService.get_by_company_id(
        db=db, company_id=company_id)


@router.post('/create_list')
async def create_list_connection(dataList: List[ConnectionCreate], db: Session = Depends(get_db)):
    new_connectons = []
    for data in dataList:
        new_conn = ConnectionService.create_connection(data=data, db=db)
        new_connectons.append(new_conn)
    return new_connectons
