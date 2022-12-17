from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database


dbMusica = SQLAlchemy() 
db_addr = "localhost"
db_user = "root" #input(f"Username of {db_addr}: ")
db_pass = "admin" #getpass(f"Password of {db_user}@{db_addr}: ")
db_name ="music"
    
# juntalo 
url = f"mysql://{db_user}:{db_pass}@{db_addr}/{db_name}"
# Create an engine object.
engine = create_engine(url, echo=True)
# Create database if it does not exist.
if not database_exists(engine.url):
    create_database(engine.url)
else:
    # Connect the database if exists.
    engine.connect()



def insertarValoresPorDefecto():
    sql = "CREATE DATABASE IF NOT EXISTS music"
    sql2 = "USE music"
    sql3 = "CREATE TABLE IF NOT EXISTS Artistas (id int NOT NULL, nombre char(255),  anyoInicio int, integrantes char(255), caratula char(255), PRIMARY KEY (id))"
    sql4 = "CREATE TABLE IF NOT EXISTS Discos" + "(id int NOT NULL," + "nombre char(255)," + "idArtista int," +  "album char(255)," + "fechaLanzamiento char(255)," + "duracion char(255)," + "genero char(255)," + "caratula char(255)," + "PRIMARY KEY (id)" + ")"
    sql5 = "INSERT IGNORE INTO Artistas (id, nombre,anyoInicio,integrantes,caratula)" + "VALUES (0,'Twenty One Pilots',2009,'Tyler Joseph Josh Dun','https://www.thebackstage.net/wp-content/uploads/2015/04/twentyonepilots.promo1-JabariJacobs-scaled.jpg');"
    sql6 = "INSERT IGNORE INTO Artistas (id, nombre,anyoInicio,integrantes,caratula)" + "VALUES (1,'Panic at the disco!',2004,'Brendon Urie','https://i0.wp.com/www.scienceofnoise.net/wp-content/uploads/2022/10/Panic-At-The-Disco.jpeg');"
    sql7 = "INSERT IGNORE INTO Artistas (id, nombre,anyoInicio,integrantes,caratula)" + "VALUES (2,'Bearoid',2015,'Dani Belenguer','https://verlanga.com/wp-content/uploads/Bearoid.jpg');"
    sql8 = "INSERT IGNORE INTO Artistas (id, nombre,anyoInicio,integrantes,caratula)" + "VALUES (3,'Besmaya',2020,'Javier Echari, Javier Olanguren','https://proximosingle.com/wp-content/uploads/2022/08/besmaya-proximo-single-1000x600.jpg');"
    sql9 = "INSERT IGNORE INTO Discos (id, nombre, idArtista, album, fechaLanzamiento, duracion, genero, caratula)" + "VALUES('0','Saturday','0','Scaled and Icy','2021','3:50','Alternativo','https://m.media-amazon.com/images/I/81RYxWS3npL._SL1425_.jpg')"
    sql10 = "INSERT IGNORE INTO Discos (id, nombre, idArtista, album, fechaLanzamiento, duracion, genero, caratula)" + "VALUES('1','Shy Away','0','Scaled and Icy','2021','3:21','Alternativo','https://m.media-amazon.com/images/I/81RYxWS3npL._SL1425_.jpg')"
    sql11 = "INSERT IGNORE INTO Discos (id, nombre, idArtista, album, fechaLanzamiento, duracion, genero, caratula)" + "VALUES('2','Never Take It','0','Scaled and Icy','2021','3:34','Alternativo','https://m.media-amazon.com/images/I/81RYxWS3npL._SL1425_.jpg')"
    sql12 = "INSERT IGNORE INTO Discos (id, nombre, idArtista, album, fechaLanzamiento, duracion, genero, caratula)" +"VALUES('3','Ride','0','Blurryface','2015','3:47','Rock','https://i.discogs.com/jTxcshLNsZ2M6oZtldVux22Bd_vgKdK86jOHfdyWt-8/rs:fit/g:sm/q:90/h:600/w:595/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTIwNjE3/MzY2LTE2NDQyNDQz/MDAtOTg5NC5qcGVn.jpeg')"

    sqls = [sql,sql2,sql3,sql4,sql5,sql6,sql7,sql8,sql9,sql10,sql11,sql12]

    with engine.connect() as con:
        for sentencia in sqls:
            rs = con.execute(sentencia)
            #print(rs)
    
def getArtistas():
    sql = "SELECT * FROM artistas"
    with engine.connect() as con:
        rs = con.execute(sql)
    return rs

def getCanciones():
    sql = "SELECT * FROM discos"
    with engine.connect() as con:
        rs = con.execute(sql)
    return rs

