from . import app, db
from .forms import RegistrationForm, LoginForm
from flask import render_template, url_for, redirect, flash, request
from .models import User
from passlib.hash import pbkdf2_sha256
from flask_login import login_user, current_user, logout_user
from share_now import login_man


# user loader function


@login_man.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/registration", methods=['GET', 'POST'])
def registration():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        # queries must be conveted into string before inserted in the database
        username_entered = str(reg_form.username.data).lower()
        password_entered = reg_form.password.data
        email_entered = str(reg_form.email.data).lower()

        # hashed password
        hashed_password = pbkdf2_sha256.hash(password_entered)

        # add user to db
        addUser = User(username=username_entered,
                       email=email_entered, password=hashed_password)
        db.session.add(addUser)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("registration.html", form=reg_form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if not current_user.is_authenticated:
        login_form = LoginForm()
        if login_form.validate_on_submit():
            user_object = User.query.filter_by(
                username=login_form.username.data).first()
            login_user(user_object)  # putting user into session
            if current_user.is_authenticated:
                return redirect(url_for("logged_in"))
            return "not logged in"

        return render_template("login.html", form=login_form)
    else:
        return redirect(url_for("logged_in"))


@app.route("/loggedin", methods=['GET', 'POST'])
def logged_in():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    return f"Welcome {current_user.username}"


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))
