from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# flask app instance
app = Flask(__name__)
app.config["SECRET_KEY"] = "aunsyedshah"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///share_now.db'

# database instance
db = SQLAlchemy(app)

# flask views
from . import views