var mysql = require('mysql');
var con;

function conexionar(){
  con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "admin"
  });
}


function insertarValoresPorDefecto(){

  var sql = "CREATE DATABASE IF NOT EXISTS music"
  var sql2 = "USE music"
  var sql3 = "CREATE TABLE IF NOT EXISTS Artistas (id int NOT NULL, nombre varchar(255),  anyoInicio int, integrantes varchar(255), caratula varchar(255), PRIMARY KEY (id))"
  var sql4 = "CREATE TABLE IF NOT EXISTS Discos" +
    "(id int NOT NULL," +
    "nombre varchar(255)," +
    "idArtista int," +
    "album varchar(255)," +
    "fechaLanzamiento varchar(255)," +
    "duracion varchar(255)," +
    "genero varchar(255)," +
    "caratula varchar(255)," +
    "PRIMARY KEY (id)" +
    ")";

  var sql5 = "INSERT IGNORE INTO Artistas (id, nombre,anyoInicio,integrantes,caratula)" +
    "VALUES (0,'Twenty One Pilots',2009,'Tyler Joseph Josh Dun','https://www.thebackstage.net/wp-content/uploads/2015/04/twentyonepilots.promo1-JabariJacobs-scaled.jpg');";

  var sql6 = "INSERT IGNORE INTO Artistas (id, nombre,anyoInicio,integrantes,caratula)" +
    "VALUES (1,'Panic at the disco!',2004,'Brendon Urie','https://i0.wp.com/www.scienceofnoise.net/wp-content/uploads/2022/10/Panic-At-The-Disco.jpeg');";

  var sql7 = "INSERT IGNORE INTO Artistas (id, nombre,anyoInicio,integrantes,caratula)" +
    "VALUES (2,'Bearoid',2015,'Dani Belenguer','https://verlanga.com/wp-content/uploads/Bearoid.jpg');"

  var sql8 = "INSERT IGNORE INTO Artistas (id, nombre,anyoInicio,integrantes,caratula)" +
    "VALUES (3,'Besmaya',2020,'Javier Echavarri, Javier Olanguren','https://proximosingle.com/wp-content/uploads/2022/08/besmaya-proximo-single-1000x600.jpg');"

  var sql9 = "INSERT IGNORE INTO Discos (id, nombre, idArtista, album, fechaLanzamiento, duracion, genero, caratula)" +
    "VALUES('0','Saturday','0','Scaled and Icy','2021','3:50','Alternativo','https://m.media-amazon.com/images/I/81RYxWS3npL._SL1425_.jpg')";

  var sql10 = "INSERT IGNORE INTO Discos (id, nombre, idArtista, album, fechaLanzamiento, duracion, genero, caratula)" +
    "VALUES('1','Shy Away','0','Scaled and Icy','2021','3:21','Alternativo','https://m.media-amazon.com/images/I/81RYxWS3npL._SL1425_.jpg')";

  var sql11 = "INSERT IGNORE INTO Discos (id, nombre, idArtista, album, fechaLanzamiento, duracion, genero, caratula)" +
    "VALUES('2','Never Take It','0','Scaled and Icy','2021','3:34','Alternativo','https://m.media-amazon.com/images/I/81RYxWS3npL._SL1425_.jpg')";

  var sql12 = "INSERT IGNORE INTO Discos (id, nombre, idArtista, album, fechaLanzamiento, duracion, genero, caratula)" +
    "VALUES('3','Ride','0','Blurryface','2015','3:47','Rock','https://i.discogs.com/jTxcshLNsZ2M6oZtldVux22Bd_vgKdK86jOHfdyWt-8/rs:fit/g:sm/q:90/h:600/w:595/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTIwNjE3/MzY2LTE2NDQyNDQz/MDAtOTg5NC5qcGVn.jpeg')";


  con.connect(function (err) {
    if (err) throw err;
    console.log("Connected!");
    con.query(sql, function (err, result) {
      if (err) throw err;
      console.log("Result: " + result);
    });
    con.query(sql2, function (err, result) {
      if (err) throw err;
      console.log("Result: " + result);
    });
    con.query(sql3, function (err, result) {
      if (err) throw err;
      console.log("Result: " + result);
    });
    con.query(sql4, function (err, result) {
      if (err) throw err;
      console.log("Result: " + result);
    });
    con.query(sql5, function (err, result) {
      if (err) throw err;
      console.log("Result: " + result);
    });
    con.query(sql6, function (err, result) {
      if (err) throw err;
      console.log("Result: " + result);
    });
    con.query(sql7, function (err, result) {
      if (err) throw err;
      console.log("Result: " + result);
    });
    con.query(sql8, function (err, result) {
      if (err) throw err;
      console.log("Result: " + result);
    });
    con.query(sql9, function (err, result) {
      if (err) throw err;
      console.log("Result: " + result);
    });
    con.query(sql10, function (err, result) {
      if (err) throw err;
      console.log("Result: " + result);
    });
    con.query(sql11, function (err, result) {
      if (err) throw err;
      console.log("Result: " + result);
    });
    con.query(sql12, function (err, result) {
      if (err) throw err;
      console.log("Result: " + result);
    });
  });

  cerrarConexion(); /*Si no se cierra la conexion no es posible hacer mas selects ni inserts en otras clases*/
}


async function cerrarConexion() {
  await new Promise(resolve => setTimeout(resolve, 3000));
  con.end();
  console.log("Cerrado");
}

function getArtistas(){
  conexionar();
  
  var sql = "SELECT * FROM artistas;";

  con.connect(function (err) {
    if (err) throw err;
    console.log("Connected!");
    con.query(sql, function (err, result) {
      if (err) throw err;
      console.log("Result: " + result);
    });
  });
  
  cerrarConexion();
}

function getCancion(cancionId){
  conexionar();
    
  var sql = "SELECT duracion FROM canciones WHERE cancion id=" + cancionId + ";";

  con.connect(function (err) {
    if (err) throw err;
    console.log("Connected!");
    con.query(sql, function (err, result) {
      if (err) throw err;
      console.log("Result: " + result);
      //AQUI SE HACEN COSAS
    });
  });

  cerrarConexion();
}


