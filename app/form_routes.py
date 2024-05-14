from app import app, db
from app.model import Users
from app.forms import LoginForm, SignUpForm
from flask import render_template, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user
from sqlalchemy import desc
from werkzeug.security import generate_password_hash

@app.route("/login-request", methods=["post"])
def login_request():
    """Handles login form requests"""
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data

        user = Users.query.filter_by(Email=email).first()
        if user != None:
            if user.check_password(password):
                # Authentication successful, redirect to some page
                login_user(user)
                return redirect(url_for("games_view"))
        else:
            # Authentication failed, redirect back to login page
            flash("Invalid username or password")
            signup_form = SignUpForm({}) # {} is to init signup_form with empty data as for some reason it shares data with login_form
            return render_template("account-creation.html", title="Login or Sign Up", 
                    login_form=login_form, signup_form=signup_form)

@app.route("/signup-request", methods=["post"])
def signup_request():
    """Handles signup form requests"""
    signup_form = SignUpForm()
    if signup_form.validate_on_submit():
        username = signup_form.username.data
        password = signup_form.password.data
        email = signup_form.email.data

        user = Users.query.filter_by(Email=email).first()
        if user == None:
            # Email not in system, create new user
            user_with_last_uid=Users.query.order_by(desc(Users.UID)).first()
            new_uid = int(user_with_last_uid.UID)+1 # Gets theoretically new UID
            while Users.query.filter_by(UID=new_uid).first() != None: # Guarantees that new_uid is unique
                new_uid += 1

            user = Users(UID=new_uid, Username=username, Email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()

            login_user(user)

            return redirect(url_for("games_view"))
        else:
            # Authentication failed, redirect back to login page
            flash("Invalid Email")
            login_form = LoginForm({}) # {} is to init signup_form with empty data as for some reason it shares data with login_form
            return render_template("account-creation.html", title="Login or Sign Up", 
                    login_form=login_form, signup_form=signup_form)

@app.route("/logout-request")
@login_required
def logout_request():
    """Handles request for logging out
    
        Redirects user to the introduction page.
    """
    logout_user()
    return redirect(url_for("introduction"))