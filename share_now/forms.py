from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    """
    Registration Form
    """
    username = StringField("Username", validators=[
                           DataRequired(message="Username required"), Length(min=3, max=15)])
    email = StringField("Email", validators=[DataRequired(
        message="Please enter a valid email address"), Email()])
    password = PasswordField("Password", validators=[
                             DataRequired("Password must be between 8 to 15 characters"), Length(min=8, max=15)])
    confirm_password = PasswordField("Confirm Password", validators=[
                                     DataRequired(), EqualTo("password", message="Password must match")])
    submit = SubmitField("Register")
