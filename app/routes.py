from app import app

# Both endpoints are temporary for testing
@app.route("/")
def hello():
  return "Hello World!"

@app.route("/test/route")
def test():
  return "Testing"
