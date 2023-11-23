import requests
from bs4 import BeautifulSoup
from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.models.company import Company


class CompanyService:
    @staticmethod
    def search_company(q: str):
        # Perform a search on 'orginfo.uz' based on the query
        lst = []
        params = {'q': q}
        try:
            response = requests.get(
                'https://orginfo.uz/uz/search/Companys/', params=params)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            data_content = soup.find_all(
                'a', {"class": "text-decoration-none og-card"})

            for i in data_content:
                fmap = {}
                f_response = requests.get(f'https://orginfo.uz{i["href"]}')
                f_response.raise_for_status()
                fsoup = BeautifulSoup(f_response.text, "html.parser")
                f_content = fsoup.find(
                    "div", {"class": "col-12 col-lg-9 m-auto printable"})
                name = f_content.find_all("h5")[0].text
                fmap["name"] = name

                f_content = f_content.find_all(
                    'div', {"class": "row border-bottom py-3"})
                key = True
                key_str = ""

                for j in f_content:
                    for matn in j.find_all('span'):
                        if key:
                            key_str = matn.text.strip()
                        else:
                            if key_str == "Telefon raqami":
                                value = matn.text.strip()
                                fmap.update({"phone_number": value})
                            else:
                                value = matn.text.strip()
                                fmap.update({key_str.lower(): value})
                        key = not key

                lst.append(fmap)
        except requests.RequestException as e:
            # Handle request exceptions here
            print(f"Request Exception: {e}")

        return lst

    @staticmethod
    def get_all_companys(db: Session):
        return db.query(Company).filter(Company.is_active == True).all()

    @staticmethod
    async def create_company(data, db: Session):
        if CompanyService.get_company_by_stir(data.stir, db):
            raise HTTPException(
                status_code=422, detail="Bu STIR li foydalanuvchi allaqachon mavjud"
            )
        obj = Company(
            name=data.name,
            stir=data.stir,
            phone_number=data.phone_number
        )
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    async def update_company(stir, data, db: Session):
        instance = CompanyService.get_company_by_stir(stir=stir, db=db)
        instance.name = data.name
        instance.phone_number = data.phone_number
        db.commit()
        db.refresh(instance)
        return instance

    @staticmethod
    def delete_company(instance, db: Session):
        instance.is_active = False
        db.commit()
        return True

    @staticmethod
    def get_company_by_stir(stir: int, db: Session):
        company = db.query(Company).filter(Company.stir == stir).first()
        if not company:
            raise HTTPException(
                status_code=404, detail="not found"
            )
        return company

    @staticmethod
    def get_company_by_id(id: int, db):
        return db.query(Company).filter(Company.id == id).first()
