from fastapi import APIRouter
from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class blogType(str, Enum):
    story = 'story'
    short = 'short'
    howto = 'howto'

@router.get(
        '/all',
        summary="retrieve all blogs",
        description="idek bruh"
        )
def get_all_blogs(page = 1, page_size = 10):
    return {'message' : f'all {page_size} on page {page}'}

@router.get('/type/{type}', tags=['blog'])




@router.get('/blog/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    """
    - **this** is the description dont ask me what this thing even does i already forgot
    """
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error' : f' Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with id {id}'}
