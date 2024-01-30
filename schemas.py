from pydantic import BaseModel
from typing import Optional
from decouple import config

class SignUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    class Config:
        orm_mode = True
        schema_extra = {
            'example':{
                'username':'welicodev',
                'email':config("EMAIL"),
                'password':config("PASSWORD"),
                'is_staff':False,
                'is_active':True
            }
        }

class Settings(BaseModel):
    authjwt_secret_key = 'd4ce71bba412cbc9d3eacbaabd7836dc6a2c96d6268385987eb5a3939debb75f'

class LoginModel(BaseModel):
    username_or_email: str
    password: str

class OrderModel(BaseModel):
    id: Optional[int]
    quantity: int
    order_statuses: Optional[int] = "PENDING"
    user_id: Optional[int]
    product_id: int

    class Config:
        orm_model = True
        schema_extra = {
            "example":{
                "quantity":2,
            }
        }

class OrderStatusModel(BaseModel):
    order_statuses: Optional[str] = "PENDING"

    class Config:
        orm_model = True
        schema_extra = {
            "example":{
                "order_statuses":"PENDING",
            }
        }


class ProductModel(BaseModel):
    id: Optional[int]
    name: str
    price: int

    class Config:
        orm_model = True
        schema_extra = {
            "example":{
                "name":"Choyxona Palov",
                "price":40000
            }
        }
