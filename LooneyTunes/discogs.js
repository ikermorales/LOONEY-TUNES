import Discojs from 'discojs'

const client = new Discojs({
  userToken: process.env.USER_TOKEN,
})

client
  .searchArtist('Jacob Desvarieux')
  .then(data => doSomethingWith(data))