from share_now import db
# step 2
from flask_login import UserMixin


class User(UserMixin, db.Model):
    """
    User Model
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
