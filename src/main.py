"""Main file."""

from flask import Flask, redirect, render_template, request
from manager.password import Encryptor

app = Flask(__name__, template_folder="app/templates")


@app.route("/")
def base():
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    elif request.method == "POST":
        if (
            request.form.get("username") is not None
            and request.form.get("password") is not None
        ):
            username = request.form.get("username")
            password = request.form.get("password")
            if username == "hmsf" and password == "admin":
                return "Success!"
            else:
                return "Failed."
        else:
            return "Cannot leave fields blank."


@app.route("/index")
def index():
    return "Welcome to Password Manager."


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
