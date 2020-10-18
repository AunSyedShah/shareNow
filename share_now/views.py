from . import app
from .forms import RegistrationForm
from flask import render_template, url_for, redirect


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/registration", methods=['GET', 'POST'])
def registration():
    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():
        return redirect(url_for("index"))
    return render_template("registration.html", form=registration_form)
