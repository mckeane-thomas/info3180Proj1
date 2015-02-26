import os
import sys

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy



db=SQLAlchemy(app)



from app import views,models
