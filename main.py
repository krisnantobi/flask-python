from flask import Flask
from routes.users import init_user_routes

app = Flask(__name__)

app.config.from_pyfile('./config/development.cfg')
init_user_routes(app)