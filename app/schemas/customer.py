from pydantic import BaseModel


class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str | None = None


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(CustomerBase):
    pass


class CustomerResponse(CustomerBase):
    id: int

    class Config:
        from_attributes = True