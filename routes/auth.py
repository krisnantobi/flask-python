import json
import token
from flask import redirect, request, session, url_for
from flask.blueprints import Blueprint
from authlib.integrations.flask_client import OAuth
from app.controllers.OAuthController import OAuthController as Controller

def init_auth_routes(app):
    auth_route = Blueprint('auth_route', __name__)
    
    oauth = OAuth(app)
    oauth.register(
        name='google',
        client_id=app.config.get("GOOGLE_CLIENT_ID"),
        client_secret=app.config.get("GOOGLE_CLIENT_SECRET"),
        access_token_url='https://accounts.google.com/o/oauth2/token',
        access_token_params=None,
        authorize_url='https://accounts.google.com/o/oauth2/auth',
        authorize_params=None,
        api_base_url='https://www.googleapis.com/oauth2/v1/',
        userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
        client_kwargs={'scope': 'openid email profile'},
    )

    @auth_route.route('/login')
    def login():
        redirect_uri = url_for('auth_route.authorize', _external=True)
        return oauth.google.authorize_redirect(redirect_uri)

    @auth_route.route('/authorize')
    def authorize():
        google = oauth.create_client('google')
        google.authorize_access_token()
        resp = google.get('userinfo')
        user_info = resp.json()
        session['profile'] = user_info
        session.permanent = True

        return Controller.insert(
            Controller,
            data=__get_data(data=user_info)
        )

    @app.route('/logout')
    def logout():
        for key in list(session.keys()):
            session.pop(key)
        return redirect('/')

    app.register_blueprint(auth_route)

def __get_data(data: dict)->dict:
    return {
        'nick_name' : data.get('given_name', ''),
        'email' : data.get('email', ''),
        'full_name' : data.get('name'),
        'last_name' : data.get('family_name'),
        'avatar' : data.get('picture', '')
    }