from contextlib import redirect_stderr
from flask import Flask, render_template, url_for, Blueprint, flash, session, redirect
from news import get_kyrgios_news

home = Blueprint("home", __name__, url_prefix='', template_folder='templates')

@home.route('/home', methods=["GET", "POST"])
def home_page():
    if "user_id" not in session:
        return redirect(url_for("index"))
    kyrgios_news = get_kyrgios_news()
    return render_template('home.html', kyrgios_news=kyrgios_news)