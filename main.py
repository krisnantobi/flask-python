import mongoengine
from flask import Flask

from routes.auth import init_auth_routes
from routes.users import init_user_routes

app = Flask(
    __name__
)
app.secret_key='Kris'

app.config.from_pyfile('./config/development.cfg')
init_user_routes(app)
init_auth_routes(app)

mongoengine.connect(
    db=app.config.get("MONGO_DB"), 
    host=app.config.get("MONGO_HOST"), 
    port=int(app.config.get("MONGO_PORT")), 
    # username=app.config.get("MONGO_USERNAME"), 
    # password=app.config.get("MONGO_PASSWORD")
)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0', 
        port=5000
    )
