from flask import flask

app = flask(__name__)
@app.route("/")
def hello():
  return "Hello, This is a basic flask app."

if __name__== "__main__":
  app.run("0.0.0.0")
