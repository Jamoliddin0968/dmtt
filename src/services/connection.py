from sqlalchemy.orm import Session

from src.models.connection import Connection


class ConnectionService:
    @staticmethod
    def create_connection(db: Session, product_id: int, company_id: int, dmtt_id: int) -> Connection:
        new_connection = Connection(
            product_id=product_id, company_id=company_id, dmtt_id=dmtt_id)
        db.add(new_connection)
        db.commit()
        db.refresh(new_connection)
        return new_connection

    @staticmethod
    def get_connection_by_id(db: Session, connection_id: int) -> Connection:
        return db.query(Connection).filter(Connection.id == connection_id).first()

    @staticmethod
    def delete_connection(db: Session, connection_id: int):
        db.query(Connection).filter(Connection.id == connection_id).delete()
        db.commit()
