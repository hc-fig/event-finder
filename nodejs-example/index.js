var port = 8000;
var express = require('express');
var app = express();

var http = require('http').Server(app);
app.use(express.static(__dirname));

app.get('/', function(req, res) {
    res.send('Hello World!');
});
      


app.listen(port, () => console.log('Example app listening on port 3000!'));
