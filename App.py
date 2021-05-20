import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_restful import Api

import __data__ as data
# this is a class to use so we are going to have one class instance
from assets.constants import Constants, EnvironmentVariables
from database.db import initialize_db
from routes.routes import initialize_routes

app = Flask(data.__app_name__)
app.config[Constants.JWT_SECRET_KEY] = os.environ[EnvironmentVariables.SECRET_KEY]
app.config[Constants.MONGODB_SETTINGS] = {
    'host': os.environ[EnvironmentVariables.CONNECTION_STRING]
}
app.config['JWT_TOKEN_LOCATION'] = ['headers', 'query_string']

bcrypt = Bcrypt(app)
jwt = JWTManager(app)
api = Api(app)

initialize_db(app)
initialize_routes(api)
