from pydantic import BaseModel, ConfigDict


class ConnectionBase(BaseModel):
    product_id: int
    company_id: int
    dmtt_id: int


class ConnectionCreate(ConnectionBase):
    pass


class ConnectionInfo(ConnectionBase):
    id: int

    class ConfigDict:
        from_attributes = True
