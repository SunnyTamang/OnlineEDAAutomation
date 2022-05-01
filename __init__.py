
from flask import Flask
from users.routes import users
from main.routes import main
from application_routes.routes import application
import os

from database_operations import dbOperation


def hello():
    connection = dbOperation()
    return connection.dataBaseConnection()

def create_app():
    
    
    app = Flask(__name__)
    UPLOAD_FOLDER = 'data_upload_folder'
    ALLOWED_EXTENSIONS = {'csv', 'xml', 'json'}
    # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['SECRET_KEY'] = 'this'

    app.register_blueprint(users)
    app.register_blueprint(main)
    app.register_blueprint(application)

    return app