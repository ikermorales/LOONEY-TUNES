const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello World!')
  console.log("Example2")
})

app.post('/', function(req,res){
  res.send('Hello World2!')
  console.log("Example1")
});

app.listen(port, () => {
  console.log(`Listening on port ${port}`)
})

