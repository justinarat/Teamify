from app import app,db
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm, LoginForm
from app.model import Users
from flask_login import login_user
import sys
from sqlalchemy import desc


@app.route("/")
@app.route("/introduction")
def introduction():
  return render_template("introduction.html", template_folder="templates")

@app.route("/games")
def games_view():
  return render_template("games.html")

@app.route("/lobby-searching")
def lobby_searching():
  return render_template("lobby-searching.html")

@app.route("/lobby-making")
def lobby_making():
  return render_template("lobby-making.html")

@app.route("/lobby")
def lobby_view():
  # TODO: Render the right lobby using the lobby code
  return render_template("lobby-view.html")

@app.route("/account-creation", methods=["GET", "POST"])
def account_creation():
  login_form = LoginForm()
  signup_form = SignUpForm()
  return render_template("account-creation.html", title="Login or Sign Up", login_form=login_form, signup_form=signup_form)

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

@app.route("/admin")
def admin():
  # TODO: maybe use session information (or other way) to verify the user is an admin
  return render_template("admin.html")

@app.route("/my-lobbies")
def my_lobbies():
  # TODO: Render lobbies user belongs to
  # TODO: Render lobbies user owns with choice to view them from user view or admin view
  return render_template("my-lobbies.html")
