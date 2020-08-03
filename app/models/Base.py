from mongoengine.document import Document
class Base(Document):
    meta = {
        'allow_inheritance': True,
        'abstract': True
    }