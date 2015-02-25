 import os
    _basedir = os.path.abspath(os.path.dirname(__file__))

    DEBUG = False

    SECRET_KEY = 'This string will be replaced with a proper key in production.'

    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://action@localhost/action'
    DATABASE_CONNECT_OPTIONS = {}

    THREADS_PER_PAGE = 8

    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "secretkey"
