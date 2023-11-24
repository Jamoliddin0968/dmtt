from fastapi import HTTPException
from sqlalchemy import and_
from sqlalchemy.orm import Session

from src.models.connection import Connection
from src.schemas.connection import CompanyConnectionCreate
from src.services.company import CompanyService
from src.services.dmtt import DmttService
from src.services.product import ProductService


class ConnectionService:

    @staticmethod
    async def create_company_connection(data: CompanyConnectionCreate, db):
        res_list = []
        company = CompanyService.get_company_by_id(id=data.company_id, db=db)
        data_list = data.items

        for obj in data_list:
            dmtt = DmttService.get_dmtt_by_id(id=obj.dmtt_id, db=db)
            product = ProductService.get_product_by_id(
                product_id=obj.product_id, db=db)
            new_connection = Connection(
                **obj.model_dump())
            new_connection.company_id = company.id
            db.add(new_connection)
            res_list.append(new_connection)

        db.commit()
        for connection in res_list:
            db.refresh(connection)
        return res_list

    @staticmethod
    def create_connection(db: Session, data) -> Connection:
        obj = ConnectionService.get_connection(
            company_id=data.company_id, product_id=data.product_id, dmtt_id=data.dmtt_id, db=db)
        if obj:
            return obj
        company = CompanyService.get_company_by_id(id=data.company_id, db=db)
        dmtt = DmttService.get_dmtt_by_id(id=data.dmtt_id, db=db)
        product = ProductService.get_product_by_id(
            product_id=data.product_id, db=db)
        new_connection = Connection(
            **data.model_dump())
        db.add(new_connection)
        db.commit()
        db.refresh(new_connection)
        return new_connection

    @staticmethod
    def get_connection_by_id(db: Session, connection_id: int) -> Connection:
        connection = db.query(Connection).filter(
            Connection.id == connection_id).first()
        if not connection:
            raise HTTPException(status_code=404, detail="Connection not found")
        return connection

    @staticmethod
    def get_connection(db: Session, dmtt_id, company_id, product_id) -> Connection:
        return db.query(Connection).filter(and_(Connection.dmtt_id == dmtt_id, Connection.company_id == company_id, Connection.product_id == product_id)).first()

    @staticmethod
    def delete_connection(db: Session, connection_id: int):
        db.query(Connection).filter(Connection.id == connection_id).delete()
        db.commit()

    @staticmethod
    def get_by_dmmt_id(db: Session, dmtt_id: int):
        return db.query(Connection).filter(Connection.dmtt_id == dmtt_id).all()

    @staticmethod
    def get_by_product_id(db: Session, product_id: int):
        return db.query(Connection).filter(Connection.product_id == product_id).all()

    @staticmethod
    def get_by_company_id(db: Session, company_id: int):
        return db.query(Connection).filter(Connection.company_id == company_id).all()

    @staticmethod
    def create_list_connections(db, data_list):
        pass
