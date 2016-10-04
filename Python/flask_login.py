"""
Flask login.

example.
"""
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    """Index page rendering."""
    return render_template("index.html")


@app.route("/favicon.ico")
def work_favicon():
    """Favicon processing."""
    return


@app.route("/login", methods=["POST"])
def login(name=None, passwd=None):
    """Root login page."""
    if request.method == "POST":
        if request.form["name"] == "" or request.form["passwd"] == "":
            return render_template("index.html")
        else:
            val_name = request.form["name"]
            val_pw = request.form["passwd"]
            return render_template("home.html", name=val_name, passwd=val_pw)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="7578")
