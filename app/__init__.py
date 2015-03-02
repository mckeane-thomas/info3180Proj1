from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

UPLOAD_FOLDER = 'app/static/img/profile_pics'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#app.config['SQLALCHEMY_DATABASE_URI']='postgres://dnxdmynmggyqte:HvuEMaKeFu0t6nvxcmNuf0wUIV@ec2-23-23-180-133.compute-1.amazonaws.com:5432/d255jkf0u2kot'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://action@localhost/action'
db = SQLAlchemy(app)

app.config['SECRET_KEY']="sdfhdjksfhgm nm,sfnjkdfsbdjbfkjsbbjasbhdsbfd"
#app.config.from_object('confg')

from app import views,models
