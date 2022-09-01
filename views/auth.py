from flask import Flask, render_template, url_for, Blueprint, flash, request, redirect, session
from flask_pymongo import PyMongo
mongo = PyMongo()

auth = Blueprint("auth", __name__, url_prefix='', template_folder='templates')

@auth.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        email = request.form['emaail']
        password = request.form['password']
        first = request.form['first']
        last = request.form['last']
        phone = request.form['phone']
        zip = request.form['zip']
        ntrp = request.form['ntrp']
        check_user = mongo.db.user.find_one({"email":"email"})
        if check_user:
            flash("Email already registered", 'danger')
            return redirect(url_for('auth.register'))
        else:
            mongo.db.user.insert_one({"first_name":first,
                                       "last_name":last,
                                       "password":password,
                                       "contact": {
                                            "email":email,
                                            "phone_number":phone,
                                                    },
                                       "zip_code":zip,
                                       "ntrp":ntrp,
                                       "log_count":0})
            find_user = mongo.db.user.find_one({"email":email})
            session['user_id'] = find_user.get('_id')
            flash("Successfully Registered", 'success')
            return redirect(url_for('home.home_page'))
    return render_template('register.html')

@auth.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')