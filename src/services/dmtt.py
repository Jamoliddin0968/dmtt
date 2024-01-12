from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.schemas.dmtt import DmttCreate, PersonCreate, PersonUpdate

from src.models.dmtt import Dmtt, Person


class DmttService:
    @staticmethod
    def get_all_dmtt(db):
        return db.query(Dmtt).filter(Dmtt.is_active).all()

    @staticmethod
    async def create_dmtt(data, db):
        if data.stir and DmttService.check_existing_stir(data.stir, db):
            raise HTTPException(
                status_code=422, detail="Bu STIR li foydalanuvchi allaqachon mavjud")
        obj = Dmtt(**data.model_dump())
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    async def update_dmtt(id, data, db):
        DmttService.get_dmtt_by_id(id, db)
        db.query(Dmtt).filter(Dmtt.id == id).update(data.model_dump())
        db.commit()
        return db.query(Dmtt).filter(Dmtt.id == id).first()

    @staticmethod
    def delete_dmtt(id, db):
        instance = DmttService.get_dmtt_by_id(id, db)
        instance.is_active = False
        db.commit()
        return {"detail": "delete"}

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


class DmttPersonService:
    @staticmethod
    def create_person(db: Session, person: PersonCreate):
        db_person = Person(**person.model_dump())
        db.add(db_person)
        db.commit()
        db.refresh(db_person)
        return db_person

    @staticmethod
    def get_person(db, person_id: int):
        return db.query(Person).filter(Person.id == person_id).first()

    @staticmethod
    def get_all_persons(db):
        return db.query(Person).all()

    @staticmethod
    def update_person(db, person_id: int, updates: PersonUpdate):
        db_person = db.query(Person).filter(Person.id == person_id).first()
        for key, value in updates.model_dump().items():
            setattr(db_person, key, value)
        db.commit()
        db.refresh(db_person)
        return db_person

    @staticmethod
    def delete_person(db, person_id: int):
        db_person = db.query(Person).filter(Person.id == person_id).first()
        db.delete(db_person)
        db.commit()
        return {"message": "Person deleted successfully"}
