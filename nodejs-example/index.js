// Sets what port to use. This is just a variable that will be used on the
// last line
var port = 8000;

// Import the express module. see https://medium.freecodecamp.org/requiring-modules-in-node-js-everything-you-need-to-know-e7fbd119be8
var express = require('express');

// Makes an instance of an express app
var app = express();


// This line is only necessary if you want to use socket.io
// in the future. Don't worry about it if you're not using
// socket.io
//var http = require('http').Server(app);


// Tells the app to give people stuff in the directory. For example, if I went
// to localhost:8000/index.js, I would see this file
app.use(express.static(__dirname));
// the default route, localhost:8000/, gives index.html


// Defines a route. see https://expressjs.com/en/guide/routing.html
// When the user requests localhost:8000/random/, they get what res.send
// is called with
app.get('/random/', function(req, res) {
    var random = String(Math.random());
    var message = "Your random number is " + random;
    res.send(message);
});
      

// Tells the app to host the server on port 'port'
app.listen(port, function() {
    console.log('Example app listening on port ' + port);
});
