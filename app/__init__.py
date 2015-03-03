from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

UPLOAD_FOLDER = 'app/static/img/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI']='postgres://wewdixbkvpnrco:OO5CCbiAtufjG-ab5BFzFPHWcp@ec2-54-235-80-55.compute-1.amazonaws.com:5432/dfnudduasn1gbj'
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://action@localhost/action'
db = SQLAlchemy(app)

app.config['SECRET_KEY']="sdfhdjksfhgm nm,sfnjkdfsbdjbfkjsbbjasbhdsbfd"
#app.config.from_object('confg')

from app import views,models
