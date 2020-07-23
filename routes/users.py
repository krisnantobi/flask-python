from flask import Blueprint
from flask.json import jsonify
from app.oAuth import oAuth
from .utils import json_response


def init_user_routes(app):
    user_route = Blueprint('user_route', __name__)

    @json_response
    @user_route.route('/')
    def hello_world():
        oauth = oAuth(app.config)
        data = oauth.user_oauth()
        return data

    app.register_blueprint(user_route)