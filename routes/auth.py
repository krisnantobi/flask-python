from flask.blueprints import Blueprint


def init_auth_routes(app):
    auth_route = Blueprint('auth_route', __name__)

    @auth_route.route('/auth')
    def auth():
        return {
            'token': 'Token ku'
        }, 200

    app.register_blueprint(auth_route)