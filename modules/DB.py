from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
	uuid = db.Column(db.String(36), primary_key=True)
	username = db.Column(db.String(30), unique=True, nullable=False)
	password = db.Column(db.String(30), nullable=False)
	salt = db.Column(db.String(30), nullable=False)
	max_profiles = db.Column(db.SmallInteger(), nullable=False)
	role = db.Column(db.SmallInteger(), nullable=False)
	first_login = db.Column(db.Boolean(), nullable=False)
	enabled = db.Column(db.Boolean(), nullable=False)

class Profile(db.Model):
    uuid = db.Column(db.String(36), primary_key=True)
    user_uuid = db.Column(db.String(36), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    upload = db.Column(db.Float(), nullable=False)
    download = db.Column(db.Float(), nullable=False)
    private_key = db.Column(db.Text(), nullable=False)
    public_key = db.Column(db.Text(), nullable=False)
    time_total = db.Column(db.Float(), nullable=False)
    time_current = db.Column(db.Float(), nullable=False)
    status = db.Column(db.SmallInteger(), nullable=False)

class Settings(db.Model):
    key = db.Column(db.Text(), primary_key=True)
    value = db.Column(db.Text(), nullable=False)
