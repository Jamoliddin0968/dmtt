import requests
from bs4 import BeautifulSoup

from src.models.organization import Organization


def searchOrganization(q: str):
    lst = []
    params = {
        'q': q,
    }
    response = requests.get('https://orginfo.uz/uz/search/organizations/',
                            params=params)
    soup = BeautifulSoup(response.text, "html.parser")
    data_content = soup.find_all(
        'a', {"class": "text-decoration-none og-card"})
    for i in data_content:
        fmap = {}
        fresponse = requests.get(f'https://orginfo.uz{i["href"]}',
                                 )
        fsoup = BeautifulSoup(fresponse.text, "html.parser")
        fcontent = fsoup.find(
            "div", {"class": "col-12 col-lg-9 m-auto printable"})
        name = fcontent.find_all("h5")[0].text
        fmap["name"] = name
        fcontent = fcontent.find_all(
            'div', {"class": "row border-bottom py-3"})
        key = True
        key_str = ""
        for j in fcontent:
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
    return (lst)

# new_user = models.User(name=request.name, email=request.email, password=request.password)
    # database.add(new_user)
    # database.commit()
    # database.refresh(new_user)
    # return new_user


def getAllOrganizations(db):
    return db.query(Organization).filter(Organization.is_active == True)


async def createOrganization(data, db):
    obj = Organization(
        name=data.name,
        stir=data.stir,
        phone_number=data.phone_number
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


async def updateOrganization(instance, data, db):
    instance.name = data.name
    instance.phone_number = data.phone_number
    db.commit()
    db.refresh(instance)
    return instance


def deleteOrganization(instanse, db):
    instance.is_active = False
    db.commit()
    return True
