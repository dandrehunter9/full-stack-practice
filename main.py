from fastapi import FastAPI, status, Response, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from db.database import engine
from enum import Enum
from typing import Optional
from router import blog_get
from router import blog_post
from router import user
from router import article, product
from db import models
from exceptions import StoryException

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)

@app.get('/')
def index():
    return {'message' : 'hello world'}

@app.exception_handler(StoryException)
def story_handler(request: Request, exc: StoryException):
    return JSONResponse(status_code=418, content={'detail' : exc.name})

models.Base.metadata.create_all(engine)


