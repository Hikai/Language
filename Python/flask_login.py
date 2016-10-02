"""
Flask login.

example.
"""
from flask import Flask, render_template, redirect, request
app = Flask(__name__)


@app.route('/', methods=['POST'])
def login():
    """Root login page."""
    if request.method == 'POST':
        if request.form['name'] == "" or request.form['passwd'] == "":
            return render_template("index.html")
        else:
            return redirect("home.html")

if __name__ == "__main__":
    app.run()
