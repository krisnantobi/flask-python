from flask import Flask
from routes.users import init_user_routes

app = Flask(__name__)

app.config.from_pyfile('./config/development.cfg')
app = init_user_routes(app)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0', 
        port=5000
    )