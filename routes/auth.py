import json
import token
from flask import redirect, request, session, url_for
from flask.blueprints import Blueprint
from authlib.integrations.flask_client import OAuth
from app.controllers.OAuthController import OAuthController as Controller
from .utils import login_not_required

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
    @login_not_required
    def login():
        redirect_uri = url_for('auth_route.authorize', _external=True)
        return oauth.google.authorize_redirect(redirect_uri)

    @auth_route.route('/authorize')
    def authorize():
        google = oauth.create_client('google')
        token = google.authorize_access_token()
        usr = google.parse_id_token('ya29.a0AfH6SMCJlRv6-iB8632gJug1m2hE47G0Yj3EU6CJhJOGCjuVgnrSCZTq173yAVlNIcuFQo5l2-W0hLP9id6WVQB2yRovVt-9gTa5IJbkcCIQxmC7huHBgfktiW1Rur7WgezwS6zZ__GVl_slCG-y49RwFpfqnOBIHv4')
        print(type(token))
        # resp = google.get('userinfo')
        # user_info = resp.json()
        # session['profile'] = user_info
        # session.permanent = True

        return token, 200

    @app.route('/logout')
    def logout():
        for key in list(session.keys()):
            session.pop(key)
        return redirect('/yuhu')

    app.register_blueprint(auth_route)

def __get_data(data: dict)->dict:
    return {
        'nick_name' : data.get('given_name', ''),
        'email' : data.get('email', ''),
        'full_name' : data.get('name'),
        'last_name' : data.get('family_name'),
        'avatar' : data.get('picture', '')
    }