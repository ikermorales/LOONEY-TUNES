# main.py
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./users.db"

from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_dance.contrib.github import github
from flask_login import logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from getpass import getpass

from app.models import db, login_manager
from app.oauth import github_blueprint
from mongo import get_database



db_addr = "localhost"
db_user = "root" #input(f"Username of {db_addr}: ")
db_pass = "admin" #getpass(f"Password of {db_user}@{db_addr}: ")
db_name ="users"
# join 
url = f"mysql://{db_user}:{db_pass}@{db_addr}/{db_name}"
# Create an engine object.
engine = create_engine(url, echo=True)

# Create database if it does not exist.
if not database_exists(engine.url):
    create_database(engine.url)
else:
    # Connect the database if exists.
    engine.connect()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost/users'
app.secret_key = "supersecretkey"
app.register_blueprint(github_blueprint, url_prefix="/login")
db.init_app(app)
login_manager.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/ping")
def ping():
    return jsonify(ping="pong")


@app.route("/", methods=['GET', 'POST'])
def homepage():
    return render_template("index.html")


@app.route("/github")
def login():
    if not github.authorized:
        return redirect(url_for("github.login"))
    res = github.get("/user")
    username = res.json()["login"]
    return f"You are @{username} on GitHub"


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))


@app.route("/insertuser", methods=['GET', 'POST'])
def insertUser():
    
    user = request.form.get('user')
    email = request.form.get('email')
    password = request.form.get('password')

    userNEW = {
        "_user" : user,
        "email" : email,
        "password" : password
    }
    dbname = get_database()
    #print(dbname)
    dbname.users.insert_one(userNEW)
    return render_template("_base.html")


if __name__ == "__main__":
    app.run(debug=True)


