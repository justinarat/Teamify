from app import app
from flask import render_template

# Both endpoints are temporary for testing
@app.route("/")
def hello():
  return "Hello World!"

@app.route("/test/route")
def test():
  return "Testing"

# These endpoints could be in the final ver
@app.route("/")
@app.route("/introduction")
def introduction():
  return render_template("introduction.html")

@app.route("/games")
def games_view():
  return render_template("games.html")
