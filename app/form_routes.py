from app import app, db
from app.model import Users
from app.forms import LoginForm, SignUpForm
from flask import render_template, url_for, redirect, flash
from flask_login import login_user
import sys
from sqlalchemy import desc

@app.route("/login-request", methods=["post"])
def login_request():
  """Handles login form requests"""
  login_form = LoginForm()
  if login_form.validate_on_submit():
    username = login_form.username.data
    password = login_form.password.data
    print(username, file=sys.stderr)
    print(password, file=sys.stderr)

    # Check if username and password match in the database
    user = Users.query.filter_by(Username=username, Password=password).first()
    print(user, file=sys.stderr)

    if user:
        # Authentication successful, redirect to some page
        print('Match', file=sys.stderr)
        login_user(user)
        return redirect(url_for("games_view"))
    else:
        # Authentication failed, redirect back to login page
        print('No Match', file=sys.stderr)
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
    print(username, file=sys.stderr)
    print(password, file=sys.stderr)
    print(email, file=sys.stderr)
    # Check if username and password match in the database
    user = Users.query.filter_by(Email=email).first()
    print(user, file=sys.stderr)

    if user==None:
        # email not in system
        print('New email', file=sys.stderr)
        uid=0
        tests=Users.query.order_by(desc(Users.UID)).first()#gets last uid
        tests=int(tests.UID)+1 #gets theoretically new UID
        while uid==0:
           tests2=Users.query.filter_by(UID=tests).first()#checks if uid is valid
           if tests2==None:
              uid=tests
              user=Users(UID=uid,Username=username,Password=password,Email=email)#should add way to confirm addition of user
              db.session.add(user)
              db.session.commit()
           else:
              tests=tests+1
        user = Users.query.filter_by(UID=uid).first()
        login_user(user)
        return redirect(url_for("games_view"))
    else:
        # Authentication failed, redirect back to login page
        print('Invalid Email', file=sys.stderr)
        flash("Invalid Email")
        login_form = LoginForm({}) # {} is to init signup_form with empty data as for some reason it shares data with login_form
        return render_template("account-creation.html", title="Login or Sign Up", 
                login_form=login_form, signup_form=signup_form)
    return redirect(url_for("games_view"))
