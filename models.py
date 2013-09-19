from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from app import db

engine = create_engine('sqlite:///database.db', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# set your classes here

class User(Base):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    passwd = db.Column(db.String(30))

    def __init__(self, name=None, passwd=None):
        self.name = name
        self.passwd = passwd

        """
# Standard Databases
class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60))
    pwdhash = db.Column(db.String())
    email = db.Column(db.String(60))
    activate = db.Column(db.Boolean)
    created = db.Column(db.DateTime)

    def __init__(self, username, password, email):
        self.username = username
        self.pwdhash = generate_password_hash(password)
        self.email = email
        self.activate = False
        self.created = datetime.utcnow()

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)

# Standard Forms
class signup_form(Form):
    username = TextField('Username', [validators.Required()])
    password = PasswordField('Password', [validators.Required(), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password', [validators.Required()])
    email = TextField('eMail', [validators.Required()])
    accept_tos = BooleanField('I accept the TOS', [validators.Required])

class login_form(Form):
    username = TextField('Username', [validators.Required()])
    password = TextField('Password', [validators.Required()])
"""

# create tables
Base.metadata.create_all(bind=engine)
