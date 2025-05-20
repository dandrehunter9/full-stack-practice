from fastapi import FastAPI, status, Response
from db.database import engine
from enum import Enum
from typing import Optional
from router import blog_get
from router import blog_post
from router import user
from db import models

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)

@app.get('/')
def index():
    return {'message' : 'hello world'}

models.Base.metadata.create_all(engine)


