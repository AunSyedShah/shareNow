from flask import Flask

# flask app instance
app = Flask(__name__)
app.config["SECRET_KEY"] = "aunsyedshah"


# flask views
from . import views