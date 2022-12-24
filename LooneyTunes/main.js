var mysql = require('mysql');
var con;

function conexionar(){
  con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "admin"
  });
}

async function cerrarConexion() {
  await new Promise(resolve => setTimeout(resolve, 3000));
  con.end();
  console.log("Cerrado");
}

function getCancion(cancionId){
  var sql = "USE music;";
  var sql1 = "SELECT duracion FROM discos WHERE id=" + cancionId + ";";
  
  con.connect(function (err) {
    if (err) throw err;
    console.log("Connected!");
    con.query(sql, function (err, result) {
      if (err) throw err;
      console.log("Result: " + result);
    });
    con.query(sql1, function (err, result) {
      if (err) throw err;
      console.log("Result: " + JSON.stringify(result));
    });
  });

}

const express = require('express')
const app = express()
app.use(express.json());
app.use(express.urlencoded({
  extended: true
}));
const port = 3000;

app.get('/:idCancion', (req, res) => {
  conexionar();
  getCancion(req.params.idCancion)
  res.send("Enviado");
  cerrarConexion();
  
})

app.post('/', function(req,res){
  res.send('Hello World2!')
  console.log("Example1")
});

app.listen(port, () => {
  console.log(`Listening on port ${port}`)
})

