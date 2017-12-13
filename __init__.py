from flask import Flask
from flask_restful import Api;
from flask_sqlalchemy import SQLAlchemy


application = Flask(__name__);
db = SQLAlchemy(application);
application.config.from_object('config')
api = Api(application);
