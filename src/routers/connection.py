from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.schemas.connection import ConnectionCreate, ConnectionInfo
from src.services.connection import ConnectionService

router = APIRouter(prefix='/connection', tags=["Connection"])


@router.post("/create", response_model=ConnectionInfo)
def create_connection(connection: ConnectionCreate, db: Session = Depends(get_db)):
    return ConnectionService.create_connection(db=db, **connection.dict())


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
