from pydantic import BaseModel, Field

class User(BaseModel):
    login: str = Field(max_length=20)
    password: str = Field(max_length=20)
    rights: str = Field(max_length=5, default='user')