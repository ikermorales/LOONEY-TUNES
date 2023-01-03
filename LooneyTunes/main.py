# main.py
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./users.db"
import json
import time
from flask import Flask, jsonify, render_template, request
from requests import get
import requests
from app.mongo import get_database
from app.mysql import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost/music'
app.secret_key = "supersecretkey"
dbMusica.init_app(app)
insertarValoresPorDefecto()

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

    return artistas()
    #alert("Usuario registrado correctamente.")


@app.route("/checkuser", methods=['GET', 'POST'])
def checkUser():
    dbname = get_database()
    x = dbname.users.find_one({"email": request.form.get('email'), "password": request.form.get('password')})
    print(x)
    if(x != None):
        return artistas()
        #alert("Incio de sesión correcto.")
    else:
        print("Usuario inextistente")
        return render_template("index.html")
        #alert("Este usuario no exsite.")


@app.route("/artistas", methods=['GET', 'POST'])
def artistas():
    rs = getArtistas()
    
    return render_template("_base.html", artistas=rs)


@app.route("/canciones/<int:idCancion>", methods=['GET', 'POST'])
def canciones(idCancion):

    if(idCancion != 0):
        print("El ID de canción es el: " + str(idCancion))
        response = requests.get('http://localhost:3000/' + str(idCancion))
      
        linkCancion = str(response.text)

        rs = getArtistas()
        rs2 = getCanciones()
        if(request.form.get('combo') != None):
            if(request.form.get('combo') != '-1'):
                idArtista = request.form.get('combo')
                rs2 = getCancionesFiltradas(idArtista)
        
        return render_template("canciones.html", artistas=rs, canciones=rs2, link=linkCancion)

    else:
        print("Sin cancion a reproducir")
        rs = getArtistas()
        rs2 = getCanciones()
        linkCancion = None

        if(request.form.get('combo') != None):
            if(request.form.get('combo') != '-1'):
                idArtista = request.form.get('combo')
                rs2 = getCancionesFiltradas(idArtista)

        return render_template("canciones.html", artistas=rs, canciones=rs2, link=linkCancion)

if __name__ == "__main__":
    app.run(debug=True)


