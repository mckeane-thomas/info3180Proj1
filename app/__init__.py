from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
SQLALCHEMY_DATABASE_URI='postgresql://action@localhost/action'
db=SQLAlchemy(app)

app.config['SECRET_KEY']="sdfhdjksfhgm nm,sfnjkdfsbdjbfkjsbbjasbhdsbfd"

from app import views,models
