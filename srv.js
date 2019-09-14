const express = require('express')
const app = express()
const port = 3000
const path = require('path')

app.get('/', (req, res) => res.sendFile(path.resolve('./front/index.html')))
app.get('/main.js', (req, res) => res.sendFile(path.resolve('./front/main.js'))

app.listen(port, () => console.log(`Example app listening on port ${port}!`))