from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, List
from fastapi import FastAPI, status, Response, Query, Body


router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]

class image(BaseModel):
    url: str
    alias: str

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id' : id,
        'data' : blog,
        'version' : version
        }

@router.post('/new/{id}/comment')
def create_comment(blog: BlogModel, id: int,
        comment_id: int = Query(None,
            title='id of the comment',
            description='some description for comment_id',
            alias='commentId',
            deprecated=True
            ),
            content: str = Body(..., min_length=10),
            version: Optional[List[str]] = Query(None)
        ):
    return {
        'blog' : blog,
        'id' : id,
        'comment_id' : comment_id,
        'content' : content,
        'version' : version       
    }

def required_function():
    return {'message' : 'learning'}    