from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# flask app instance
app = Flask(__name__)
app.config["SECRET_KEY"] = "aunsyedshah"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///share_now.db'

# database instance
db = SQLAlchemy(app)

# configure flask login
login_man = LoginManager(app)
# initialize app, Step 1 -> Step 2 models.py
login_man.init_app(app)

# flask views
from . import views