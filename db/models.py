from db.database import Base
from sqlalchemy import column

class DBUser(Base):
    __tablename__ = 'users'
    id = column