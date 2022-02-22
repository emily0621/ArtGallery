from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_session import Session
from sqlalchemy.orm import Query
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import config

app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

engine = create_engine('mysql://root:1234@localhost:3306/testdb', convert_unicode=True)
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

import routes





