from flask import Flask, render_template, redirect, url_for, Blueprint
from werkzeug.security import check_password_hash, generate_password_hash
from dotenv import load_dotenv
from views.auth import auth
from views.home import home

app = Flask(__name__)

app.config["SECRET KEY"] = "CHANGE THIS LATER"

app.register_blueprint(auth)
app.register_blueprint(home)


@app.route('/', methods=["POST", "GET"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)