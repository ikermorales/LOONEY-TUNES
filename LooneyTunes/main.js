var mysql = require('mysql');
var con;
var returneado = "";

function conexionar(){
  con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "root"
  });
}

async function cerrarConexion() {
  await new Promise(resolve => setTimeout(resolve, 3000));
  con.end();
  console.log("Cerrado");
}

function getCancion(cancionId, res){
  conexionar();
  
  var sql = "USE music;";
  var sql1 = "SELECT duracion FROM discos WHERE id=" + cancionId + ";";

  con.connect(function (err) {
    if (err) throw err;
    console.log("Connected!");
    con.query(sql, function (err, result) {
      if (err) throw err;
      //console.log("Result: " + result);
    });
    con.query(sql1, function (err, result) {
      if (err) throw err;
      resultado = JSON.stringify(result[0]);
      metiendo = false;
      returneado = "";
      for (let i = 0; i < resultado.length; i++) {
        if(resultado[i]=='"' && resultado[i+1]=='}'){
          break;
        }
        else if(resultado[i-1]==':' && resultado[i]=='"'){
            metiendo=true;
        } 
        else if(metiendo == true){
          returneado += resultado[i]
        }
      }
      console.log(returneado);
      cerrarConexion();
      res.send(returneado);
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
  getCancion(req.params.idCancion, res)
})

app.listen(port, () => {
  console.log(`Listening on port ${port}`)
})

