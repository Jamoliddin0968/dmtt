import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session

from src.models.organization import Organization


class OrganizationService:
    @staticmethod
    def search_organization(q: str):
        # Perform a search on 'orginfo.uz' based on the query
        lst = []
        params = {'q': q}
        try:
            response = requests.get(
                'https://orginfo.uz/uz/search/organizations/', params=params)
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
    def get_all_organizations(db: Session):
        return db.query(Organization).filter(Organization.is_active == True).all()

    @staticmethod
    async def create_organization(data, db: Session):
        obj = Organization(
            name=data.name,
            stir=data.stir,
            phone_number=data.phone_number
        )
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    async def update_organization(instance, data, db: Session):
        instance.name = data.name
        instance.phone_number = data.phone_number
        db.commit()
        db.refresh(instance)
        return instance

    @staticmethod
    def delete_organization(instance, db: Session):
        instance.is_active = False
        db.commit()
        return True

    @staticmethod
    def get_organization_by_stir(stir: int, db: Session):
        return db.query(Organization).filter(Organization.stir == stir).first()
