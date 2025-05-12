from pydantic import BaseModel, EmailStr, constr

class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=20)
    email: EmailStr

class UserRead(UserCreate):
    id: int

