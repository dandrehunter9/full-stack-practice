from fastapi import APIRouter, FastAPI, Depends
from schemas import UserBase
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user


router = APIRouter(
    prefix='/user',
    tags=['user']
)

# create user
@router.post('/')                                                                       
def create_user(request: UserBase, db: Session = Depends(get_db)):   
    return db_user.create_user(db, request)

# read user

# update user
