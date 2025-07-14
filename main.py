from fastapi import FastAPI, status, Response, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from sqlalchemy import true
from db.database import engine
from enum import Enum
from typing import Optional
from router import blog_get, blog_post, file, user, article, product
from auth import authentication
from db import models
from exceptions import StoryException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(authentication.router)
app.include_router(file.router)

@app.get('/')
def index():
    return {'message' : 'hello world'}

@app.exception_handler(StoryException)
def story_handler(request: Request, exc: StoryException):
    return JSONResponse(status_code=418, content={'detail' : exc.name})

models.Base.metadata.create_all(engine)

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credential = True,
    allow_methods = ["*"],
    allow_headers = ['*']
)

app.mount('/files', StaticFiles(directory="files"), name='files')