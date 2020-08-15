from .BaseController import BaseController
from flask.globals import session
from app.repositories.User import User as Repository
from app.schemas.User import User as Schema


class HomeController(BaseController):
    __schema = Schema

    def index(self):
        email = dict(session).get('email', None)
        return {
            'data': {
                'name': 'Krisnanto',
                'email': email
            }
        }

    def get_by_email(
        self,
        email: str
    ):
        result = self.__schema.full(
            self,
            data=Repository.get_by_email(self, email=email)
        )
        return self._response(
            data= result
            )