from .Base import Base
from app.models.User import User as Model

class User(Base):
    def insert(
        self,
        data: dict
    )->Model:
        user = Model(**data)
        return user.save().reload()
