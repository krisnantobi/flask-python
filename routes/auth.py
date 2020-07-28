import json
import token
from flask import redirect, request, session, url_for
from flask.blueprints import Blueprint
from authlib.integrations.flask_client import OAuth


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
        return redirect('/')

    app.register_blueprint(auth_route)