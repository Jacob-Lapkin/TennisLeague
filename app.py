from flask import Flask, render_template, redirect, url_for, Blueprint, session
from werkzeug.security import check_password_hash, generate_password_hash
from dotenv import load_dotenv
from views.auth import auth
from views.home import home
from views.leagues import leagues
from database import mongo
import os

load_dotenv()

app = Flask(__name__)

app.config["MONGO_URI"] = f'mongodb+srv://{os.getenv("mong_user")}:{os.getenv("mongo_pass")}@cluster0.njun9ub.mongodb.net/tennisleague?retryWrites=true&w=majority'
app.config["SECRET_KEY"] = "CHANGE THIS LATER"
mongo.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(home)
app.register_blueprint(leagues)

@app.route('/', methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route('/logout', methods=['POST', "GET"])
def logout():
    session.pop('email')
    return redirect(url_for('auth.login'))


if __name__ == "__main__":
    app.run(debug=True)