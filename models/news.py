from pydantic import BaseModel

class Content(BaseModel):
    title: str
    link: str
    pub_date: str
    description: str
    category: str
    text: str