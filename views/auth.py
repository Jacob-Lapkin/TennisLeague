from flask import Flask, render_template, url_for, Blueprint, flash

auth = Blueprint("auth", __name__, url_prefix='', template_folder='templates')

@auth.route('/register', methods=['POST', 'GET'])
def register():
    return render_template('register.html')

@auth.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')