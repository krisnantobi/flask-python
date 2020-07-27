from flask import Flask
from routes.auth import init_auth_routes
from routes.users import init_user_routes

app = Flask(
    __name__
)


app.config.from_pyfile('./config/development.cfg')
init_user_routes(app)
init_auth_routes(app)

app.run(host='localhost', port=5000)