from sqlalchemy import Column, Integer, String

from database import Base

from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String(140), nullable=False)
    hashed_password = Column(String(300), nullable=False)