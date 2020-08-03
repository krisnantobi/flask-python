from datetime import datetime
from mongoengine.fields import DateTimeField, EmailField, StringField
from .Base import Base
from mongoengine.document import Document

class User(Base):
    email = EmailField()
    nick_name = StringField(required=True)
    last_name = StringField(required=False)
    full_name = StringField(required=True)
    avatar = StringField(required=False)
    updated_at = DateTimeField(default=datetime.now, blank=True)
    meta = {
        'collection': 'user'
    }