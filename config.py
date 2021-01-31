import os

# Development
DEVELOPMENT = False
DROP_DB_ON_RUN = False

# Flask
SECRET_KEY = os.urandom(32)

# SQLAlchemy/Flask-SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'sqlite:///easyguard.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False

# Flask Session
SESSION_COOKIE_NAME = 'session'
SESSION_TYPE = 'sqlalchemy'
SESSION_USE_SIGNER = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True

# Security settings
FORCE_HTTPS = True
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True

# !!! LEAVE THIS SECTION ALONE !!!
if os.environ.get('FLASK_ENV') == 'development':
    SQLALCHEMY_ECHO = True
    DEVELOPMENT = True
    FORCE_HTTPS = False
    CSRF_COOKIE_SECURE = False
    SESSION_COOKIE_SECURE = False
    DROP_DB_ON_RUN = True
