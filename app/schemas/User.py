from app.libs.utils import safe_int
from .Base import Base

class User(Base):
    def full(self, data: dict)-> dict:
        return {
            'id': str(getattr(data, 'id', '')),
            'nick_name': getattr(data, 'nick_name', ''),
            'full_name': getattr(data, 'full_name', ''),
            'avatar': getattr(data, 'avatar', ''),
            'email': getattr(data, 'email', ''),
        }

    def brief(self, data: dict)-> dict:
        return {
            'id': str(getattr(data, 'id', '')),
            'nick_name': getattr(data, 'nick_name', ''),
            'email': getattr(data, 'email', ''),
        }
