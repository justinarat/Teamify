from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm, LoginForm
from app.model import Users
from flask_login import login_user
import sys


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
    # TODO: Use Flask Login to handle signup data
    #       Then update the database
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
