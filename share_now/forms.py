from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, Email, EqualTo, InputRequired, ValidationError
from .models import User


def invalid_credentials(form, field):
    """
    invalid credentials handling validator
    """
    username_entered = str(form.username.data).lower()
    password_entered = str(field.data)

    # check existing username
    user_object = User.query.filter_by(username=username_entered).first()
    if user_object is None:
        raise ValidationError("Username or Password is incorrect")
    elif password_entered != user_object.password:
        raise ValidationError("Username or Password is incorrect")


class RegistrationForm(FlaskForm):
    """
    Registration Form
    """
    username = StringField("Username", validators=[
                           InputRequired(message="Username required"), Length(min=3, max=15, message="Username must be between 4 to 8 characters")])
    email = StringField("Email", validators=[InputRequired(
        message="Please enter a valid email address"), Email()])
    password = PasswordField("Password", validators=[
                             InputRequired(), Length(min=8, max=15, message="Password must be between 8 to 15 characters")])
    confirm_password = PasswordField("Confirm Password", validators=[
                                     InputRequired(), EqualTo("password", message="Password must match")])
    submit = SubmitField("Register")

    # custom validators

    # custom validator to check for a duplicate username
    def validate_username(self, username):
        # check existing username
        user_object = User.query.filter_by(username=username.data).first()
        if user_object:
            raise ValidationError("Username already taken")
    def validate_email(self, email):
        """
        check existing email
        """
        user_email = User.query.filter_by(email=email.data).first()
        if user_email:
            raise ValidationError("email already taken")


class LoginForm(FlaskForm):
    """
    Login Form
    """
    username = StringField("Username ", validators=[
                           InputRequired(message="username required")])
    password = PasswordField("Password ", validators=[InputRequired(
        message="password required"), invalid_credentials])
    submit = SubmitField("Login")
