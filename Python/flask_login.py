"""
Flask login.

example.
"""
from flask import (
    Flask, redirect, render_template, request, session, url_for
)
from sqlalchemy import sessionmaker
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
    ses = sessionmaker()
    obj_ses = ses()
    query = obj_ses.query("User")
    query = query.all()
    obj_ses.commit()
    session["name"] = val_name
    session["passwd"] = val_pw
    return render_template("home.html", name=val_name, passwd=val_pw)


@app.route("/logout")
def logout():
    """Logout page."""
    pop_session("name")
    pop_session("passwd")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7578)
