from flask import Flask, render_template, url_for, Blueprint, flash, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
from database import mongo
auth = Blueprint("auth", __name__, url_prefix='', template_folder='templates')


@auth.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        first = request.form['first']
        last = request.form['last']
        phone = request.form['phone']
        zip = request.form['zip']
        ntrp = request.form['ntrp']
        check_user = mongo.db.users.find_one({"contact.email":email})
        if check_user:
            flash("Email already registered", 'danger')
            return redirect(url_for('auth.register'))
        else:
            hashed_pass = generate_password_hash(password)
            mongo.db.users.insert_one({"first_name":first,
                                       "last_name":last,
                                       "password":hashed_pass,
                                       "contact": {
                                            "email":email,
                                            "phone_number":phone,
                                                    },
                                       "zip_code":zip,
                                       "ntrp":ntrp,
                                       "log_count":0})
            current_user = email
            session['email'] = current_user
            flash("Successfully Registered", 'success')
            return redirect(url_for('home.home_page'))
    return render_template('register.html')

@auth.route('/login', methods=['POST', 'GET'])
def login():
    if "email" in session:
        return redirect(url_for('home.home_page'))
    if request.method == "POST":
        password = request.form['password']
        email = request.form['email']
        find_user = mongo.db.users.find_one({"contact.email":email})
        if not find_user:
            flash("email does not exist", "danger")
            return redirect(url_for('auth.login'))
        else:
            checked_password = check_password_hash(find_user['password'], password)
            if checked_password:
                session['email'] = email
                return redirect(url_for('home.home_page'))
            else:
                flash("password is incorrect", 'danger')
                return redirect(url_for('auth.login'))
    return render_template('login.html')