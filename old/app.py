import os
import datetime

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/bio")
def bio():
    return render_template("bio.html")

@app.route("/publications")
def publications():
    return render_template("publications.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")