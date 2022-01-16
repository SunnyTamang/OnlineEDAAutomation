from flask import Flask
from users.routes import users
from main.routes import main

from connect_database import dbOperation


def hello():
    connection = dbOperation()
    return connection.dataBaseConnection()

def create_app():
    
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'this'

    app.register_blueprint(users)
    app.register_blueprint(main)

    return app