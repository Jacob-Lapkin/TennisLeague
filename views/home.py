from contextlib import redirect_stderr
from urllib import request
from flask import Flask, render_template, url_for, Blueprint, flash, session, redirect, request
from news import get_kyrgios_news
from bson import ObjectId
from database import mongo

home = Blueprint("home", __name__, url_prefix='', template_folder='templates')

@home.route('/home', methods=["GET", "POST"])
def home_page():
    if "email" not in session:
        return redirect(url_for("auth.login"))
    email = session['email']
    current_user = mongo.db.users.find_one({"contact.email":email})
    kyrgios_news = get_kyrgios_news()
    if request.method == "POST" and 'survey' in request.form:
        mongo.db.users.update_one({'contact.email':email}, {"$set":{'tsit_survey':True}})
        flash("Thank you for your honest feedback", "success")
        return redirect(url_for('home.home_page'))
    return render_template('home.html', kyrgios_news=kyrgios_news, current_user=current_user)