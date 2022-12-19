const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello World!')
  console.log("Example")
})

app.post('/', function(req,res){
  res.send('Hello World2!')
  console.log("Example")
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})

