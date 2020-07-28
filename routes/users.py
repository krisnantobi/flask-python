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
    
    @app.route('/logout')
    def logout():
        print(list(session.keys()))
        for key in list(session.keys()):
            session.pop(key)
        return redirect('/')

    app.register_blueprint(user_route)
    return app