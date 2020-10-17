from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class RegistrationForm(FlaskForm):
    """
    Registration Form
    """
    username = StringField("Username", validators=[DataRequired(), Length(4, 8)])
    submit = SubmitField("Submit")