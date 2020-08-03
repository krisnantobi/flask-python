from .BaseController import BaseController
from app.repositories.User import User as Repository
from app.schemas.User import User as Schema

class OAuthController(BaseController):
    __schema = Schema

    def insert(
        self,
        data: dict
    )->dict:
        result = self.__schema.full(
            self,
            data=Repository.insert(self, data=data)
        )
        return self._response(
            data= result
            )