from flask import Blueprint
from flask.json import jsonify
from app.controllers.HomeController  import HomeController
from .utils import json_response


def init_user_routes(app):
    user_route = Blueprint('user_route', __name__)

    @user_route.route('/')
    @json_response
    def index():
        controller = HomeController()
        data = controller.index()
        return data

    app.register_blueprint(user_route)
    return app