
from src.models.dmtt import Dmtt


def getAllDmtt(db):
    users = db.query(Dmtt).filter(Dmtt.is_active == True).all()
    return users


async def createDmtt(data, db):
    obj = Dmtt(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


async def updateDmtt(stir, data, db):
    db.query(Dmtt).filter(Dmtt.stir == stir).update(data.dict())
    db.commit()
    return db.query(Dmtt).filter(Dmtt.stir == stir).first()


def deleteDmtt(instance, db):
    instance.is_active = False
    db.commit()
    return True
