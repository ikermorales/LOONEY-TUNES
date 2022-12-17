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

    sql13 = "INSERT IGNORE INTO Discos (id, nombre, idArtista, album, fechaLanzamiento, duracion, genero, caratula)" + "VALUES('4','Mi Nombre','2','Mi Nombre','2022','2:58','Pop','https://m.media-amazon.com/images/I/61EdOuf7RKL._UXNaN_FMjpg_QL85_.jpg')"
    sql14 = "INSERT IGNORE INTO Discos (id, nombre, idArtista, album, fechaLanzamiento, duracion, genero, caratula)" + "VALUES('5','U OK?','2','U OK?','2022','2:53','Pop','https://i.scdn.co/image/ab67616d0000b273d484ec70f07dff09517e4ca4')"
    sql15 = "INSERT IGNORE INTO Discos (id, nombre, idArtista, album, fechaLanzamiento, duracion, genero, caratula)" + "VALUES('6','Te doy igual','2','Te doy igual','2022','2:25','Pop','https://i.scdn.co/image/ab67616d0000b273ac447bb5f6675d63445bfc4c')"
    sql16 = "INSERT IGNORE INTO Discos (id, nombre, idArtista, album, fechaLanzamiento, duracion, genero, caratula)" + "VALUES('7','Comer','2','Ultravida','2019','2:34','Pop','https://i.scdn.co/image/ab67616d0000b2738095afa848bbe92f178f117c')"

    sql17 = "INSERT IGNORE INTO Discos (id, nombre, idArtista, album, fechaLanzamiento, duracion, genero, caratula)" + "VALUES('8','Frágiles','3','BESMAYA','2022','2:45','Pop','https://i.scdn.co/image/ab67616d0000b273706b3d5864c29d240cf40960')"
    sql18 = "INSERT IGNORE INTO Discos (id, nombre, idArtista, album, fechaLanzamiento, duracion, genero, caratula)" + "VALUES('9','Me dará igual','3','BESMAYA','2022','2:21','Pop','https://i.scdn.co/image/ab67616d0000b273706b3d5864c29d240cf40960')"
    sql19 = "INSERT IGNORE INTO Discos (id, nombre, idArtista, album, fechaLanzamiento, duracion, genero, caratula)" + "VALUES('10','Honey','3','Honey','2021','2:39','Pop','https://m.media-amazon.com/images/I/511azFeyUjS._UXNaN_FMjpg_QL85_.jpg')"
    sql20 = "INSERT IGNORE INTO Discos (id, nombre, idArtista, album, fechaLanzamiento, duracion, genero, caratula)" + "VALUES('11','Matar la Pena','3','Matar la Pena','2021','2:32','Pop','https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/ec/f9/d7/ecf9d7f6-da61-efb1-c41a-34dd6fe719a9/cover.jpg/1200x1200bf-60.jpg')"

    sql21 = "INSERT IGNORE INTO Discos (id, nombre, idArtista, album, fechaLanzamiento, duracion, genero, caratula)" + "VALUES('12','Victorius','1','Death of a Bachelor','2016','2:58','Pop/Rock','https://m.media-amazon.com/images/I/81hKk1Evy+L._SL1422_.jpg')"
    sql22 = "INSERT IGNORE INTO Discos (id, nombre, idArtista, album, fechaLanzamiento, duracion, genero, caratula)" + "VALUES('13','Roaring 20s','1','Pray for the Wicked','2018','3:05','Pop/Rock','https://m.media-amazon.com/images/I/81z-ZX-MidL._SL1400_.jpg')"
    sql23 = "INSERT IGNORE INTO Discos (id, nombre, idArtista, album, fechaLanzamiento, duracion, genero, caratula)" + "VALUES('14','Girls / Girls / Boys','1','Too Weird to Live, Too Rare to Die!','2013','3:01','Pop/Rock','https://m.media-amazon.com/images/I/71kEcR-mVHL._SL1425_.jpg')"
    sql24 = "INSERT IGNORE INTO Discos (id, nombre, idArtista, album, fechaLanzamiento, duracion, genero, caratula)" + "VALUES('15','Nine in the Afternoon','1','Pretty. Odd.','2008','3:12','Pop/Rock','https://m.media-amazon.com/images/I/91uy5qGrdNL._SL1425_.jpg')"

    sqls = [sql,sql2,sql3,sql4,sql5,sql6,sql7,sql8,sql9,sql10,sql11,sql12,sql13,sql14,sql15,sql16,sql17,sql18,sql19,sql20,sql21,sql22,sql23,sql24]

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

def getCancionesFiltradas(idArtista):
    sql = "SELECT * FROM discos WHERE idArtista ='" + idArtista + "';"
    with engine.connect() as con:
        rs = con.execute(sql)
    return rs

