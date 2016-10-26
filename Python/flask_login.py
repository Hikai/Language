"""
Flask login.

example.
"""
from flask import (
    Flask, render_template, request, Session
)
app = Flask(__name__)


def pop_session(val_session):
    """Session value pop."""
    session.pop(val_session, None)


@app.route('/')
def index():
    """Index page rendering."""
    return render_template("index.html")


@app.route("/favicon.ico")
def favicon():
    """Reqeust favicon 404 escape."""
    return


@app.route("/login", methods=["POST"])
def login(name=None, passwd=None):
    """Root login page."""
    if request.method != "POST":
        return render_template("index.html")
    else:
        if request.form["name"] == "" or request.form["passwd"] == "":
            return render_template("index.html")
    val_name = request.form["name"]
    val_pw = request.form["passwd"]
    session["name"] = val_name
    session["passwd"] = val_pw
    return render_template("home.html", name=val_name, passwd=val_pw)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7578)
