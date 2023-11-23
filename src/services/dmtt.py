from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.models.dmtt import Dmtt


class DmttService:
    @staticmethod
    def get_all_dmtt(db):
        return db.query(Dmtt).filter(Dmtt.is_active).all()

    @staticmethod
    async def create_dmtt(data, db):
        if DmttService.check_existing_stir(data.stir, db):
            raise HTTPException(
            status_code=422, detail="Bu STIR li foydalanuvchi allaqachon mavjud")
        obj = Dmtt(**data.model_dump())
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    async def update_dmtt(id, data, db):
        instance = DmttService.get_dmtt_by_id(id, db)
        db.query(Dmtt).filter(Dmtt.id == id).update(data.model_dump())
        db.commit()
        return db.query(Dmtt).filter(Dmtt.id == id).first()

    @staticmethod
    def delete_dmtt(id, db):
        instance = DmttService.get_dmtt_by_id(id, db)
        instance.is_active = False
        db.commit()
        return {"detail":"delete"}

    @staticmethod
    def check_existing_stir(stir: str, db: Session) -> bool:
        return db.query(Dmtt).filter(Dmtt.stir == stir).first() is not None

    @staticmethod
    def get_dmtt_by_stir(stir: str, db: Session):
        return db.query(Dmtt).filter(Dmtt.stir == stir).first()

    @staticmethod
    def get_dmtt_by_id(id: int, db):
        dmtt = db.query(Dmtt).filter(Dmtt.id == id).first()
        if not dmtt:
            raise HTTPException(
                status_code=404,
                detail="Bunday id li dmtt yo'q"
            )
        return dmtt
