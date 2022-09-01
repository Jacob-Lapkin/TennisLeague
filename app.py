from flask import Flask, render_template, redirect, url_for, Blueprint
from werkzeug.security import check_password_hash, generate_password_hash
from dotenv import load_dotenv
from views.auth import auth, mongo
from views.home import home
from flask_pymongo import PyMongo
import os

load_dotenv()

app = Flask(__name__)

app.config["MONGO_URI"] = f'mongodb+srv://{os.getenv("mong_user")}:{os.getenv("mongo_pass")}@cluster0.njun9ub.mongodb.net/tennisleague?retryWrites=true&w=majority'
app.config["SECRET KEY"] = "CHANGE THIS LATER"

mongo.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(home)



@app.route('/', methods=["POST", "GET"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)