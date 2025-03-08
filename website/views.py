from flask import Blueprint, render_template, redirect, url_for

views = Blueprint("views", __name__)

@views.route("/home")
@views.route("/")
def home():
    return render_template("home.html")

@views.route("/login")
def login():
    return render_template("login.html")

@views.route("/signup")
def signup():
    return render_template("signup.html")

@views.route("/logout")
def logout():
    return redirect(url_for("views.home"))