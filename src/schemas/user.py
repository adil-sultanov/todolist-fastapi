from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    name: str = Field(min_length=1, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8, max_length=50)
    age: int | None = Field(default=None, ge=1, le=100)

class UserUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=50)
    age: int | None = Field(default=None, ge=1, le=100)

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    age: int | None = None

    model_config = {"from_attributes": True}

class UserChangePassword(BaseModel):
    current_password: str
    new_password: str = Field(min_length=8, max_length=50) 