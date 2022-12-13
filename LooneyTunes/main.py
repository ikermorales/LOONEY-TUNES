# main.py
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./users.db"

from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from getpass import getpass

from app.mongo import get_database

"""
db = SQLAlchemy()


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

with app.app_context():
    db.create_all()

"""
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost/users'
#app.secret_key = "supersecretkey"
#db.init_app(app)

@app.route("/ping")
def ping():
    return jsonify(ping="pong")


@app.route("/", methods=['GET', 'POST'])
def homepage():
    return render_template("index.html")


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
    #alert("Usuario registrado correctamente.")


@app.route("/checkuser", methods=['GET', 'POST'])
def checkUser():
    dbname = get_database()
    x = dbname.users.find_one({"email": request.form.get('email'), "password": request.form.get('password')})
    print(x)
    if(x != None):
        return render_template("_base.html")
        #alert("Incio de sesión correcto.")
    else:
        print("Usuario inextistente")
        return render_template("index.html")
        #alert("Este usuario no exsite.")


if __name__ == "__main__":
    app.run(debug=True)


