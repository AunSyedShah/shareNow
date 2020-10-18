from . import app, db
from .forms import RegistrationForm
from flask import render_template, url_for, redirect
from .models import User


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/registration", methods=['GET', 'POST'])
def registration():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        # queries must be conveted into string before inserted in the database
        username_entered = str(reg_form.username.data)
        password_entered = str(reg_form.password.data)
        email_entered = str(reg_form.email.data)

        # add user to db
        addUser = User(username=username_entered,
                       email=email_entered, password=password_entered)
        db.session.add(addUser)
        db.session.commit()
        return "Inserted into database"
    return render_template("registration.html", form=reg_form)
