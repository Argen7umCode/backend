from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String
from typing import Optional


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(sa_column=Column("username", String, unique=True))
    password: str = Field(sa_column=Column("password", String, unique=True))
