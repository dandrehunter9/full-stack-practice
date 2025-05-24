from pydantic import BaseModel
from typing import List

#Article inside of the UserDisplay
class Article(BaseModel):
    title: str
    content: str
    published

class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article] = {}
    class Config():
        orm_mode = True