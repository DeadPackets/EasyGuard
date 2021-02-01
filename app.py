import os
from flask import Flask, session
from flask_session.__init__ import Session
from flask_talisman import Talisman, DENY
from flask_seasurf import SeaSurf

# Database import
from modules.DB import db

# Initialize flask
app = Flask(__name__)
app.config.from_object('config')

# Initialize Flask-Talisman for security headers
csp = {
	'default-src': '\'self\''
}
Talisman(app,
	content_security_policy=csp, frame_options=DENY,
	force_https=app.config['FORCE_HTTPS'],
	strict_transport_security=app.config['FORCE_HTTPS'],
	session_cookie_secure=app.config['SESSION_COOKIE_SECURE'])

# Initialize Flask-SeaSurf for CSRF
csrf = SeaSurf(app)

# Initialize SQLAlchemy
db.init_app(app)
if app.config['DROP_DB_ON_RUN']:
    db.drop_all(app=app)

# Set up flask sessions
SESSION_SQLALCHEMY = db
app.config.from_object(__name__)
Session(app)

# Setup the database
db.create_all(app=app)
app.app_context().push()

# With the database setup, import extra modules
from modules.DataHandler import *
from modules.vpn import VPN

# Flask routes
@app.route('/', methods=['GET'])
def main():
    return 'Hello'