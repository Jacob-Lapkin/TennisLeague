from flask import Flask, render_template, url_for, Blueprint, flash

home = Blueprint("home", __name__, url_prefix='', template_folder='templates')

@home.route('/home', methods=["GET", "POST"])
def home_page():
    return render_template('home.html')