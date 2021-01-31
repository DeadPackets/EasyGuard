import os
from flask import Flask, session
from flask_session.__init__ import Session
from flask_talisman import Talisman, DENY
from flask_seasurf import SeaSurf

# Library imports
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

# Set up flask sessions
Session(app)