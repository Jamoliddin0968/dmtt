from sqlalchemy.orm import Session

from src.models.dmtt import Dmtt


class DmttService:
    @staticmethod
    def get_all_dmtt(db):
        return db.query(Dmtt).filter(Dmtt.is_active).all()

    @staticmethod
    async def create_dmtt(data, db):
        obj = Dmtt(**data.model_dump())
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    async def update_dmtt(stir, data, db):
        db.query(Dmtt).filter(Dmtt.stir == stir).update(data.model_dump())
        db.commit()
        return db.query(Dmtt).filter(Dmtt.stir == stir).first()

    @staticmethod
    def delete_dmtt(instance, db):
        instance.is_active = False
        db.commit()
        return True

    @staticmethod
    def check_existing_stir(stir: str, db: Session) -> bool:
        return db.query(Dmtt).filter(Dmtt.stir == stir).first() is not None

    @staticmethod
    def get_dmtt_by_stir(stir: str, db: Session):
        return db.query(Dmtt).filter(Dmtt.stir == stir).first()
