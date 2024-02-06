from datetime import datetime
from typing_extensions import TypedDict

from pydantic import BaseModel


class Comment(BaseModel):
    """Модель сайта"""
    id: int
    user_id: int
    site_id: int
    text: str
    created_at: datetime


class CommentDict(TypedDict):
    """Словарь принимаемых аргументов"""
    user_id: int
    site_id: int
    text: str
