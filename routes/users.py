from flask import Blueprint, redirect, session
from flask.json import jsonify
from app.controllers.HomeController import HomeController
from .utils import check_key, json_response, login_required


def init_user_routes(app):
    user_route = Blueprint('user_route', __name__)

    @user_route.route('/')
    @login_required
    @json_response
    def index():
        controller = HomeController()
        data = controller.index()
        return data

    @user_route.route('/yuhu')
    @json_response
    def index1():
        controller = HomeController()
        data = controller.index()
        return data

    @user_route.route('/my-profile')
    @login_required
    @json_response
    def profile():
        controller = HomeController()
        if check_key(session, 'profile'):
            data = controller.get_by_email(
                dict(session['profile']).get('email', '')
            )
            return data
        return 'Failed', 400
    
    app.register_blueprint(user_route)
    return app