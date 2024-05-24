from pydantic import BaseModel, Field, EmailStr
from uuid import UUID

class User(BaseModel):
    login: str = Field(max_length=20)
    email: EmailStr = Field(max_length=50)
    password: str = Field(max_length=20)
    rights: str = Field(max_length=5, default='user')
    
class UserResponse(BaseModel):
    id: UUID
    login: str
    email: EmailStr
    rights: str