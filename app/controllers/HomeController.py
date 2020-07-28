from flask.globals import session


class HomeController():
    def index(self):
        email = dict(session).get('email', None)
        return {
            'data': {
                'name': 'Krisnanto',
                'email': email
            }
        }