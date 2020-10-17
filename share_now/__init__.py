from flask import Flask

# flask app instance
app = Flask(__name__)


# flask views
from . import views