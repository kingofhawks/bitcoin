var app = require('http').createServer(handler)
  , io = require('socket.io').listen(app)
  , fs = require('fs')

app.listen(80);

var redis = require('socket.io/node_modules/redis');
var sub = redis.createClient(6379,'192.168.192.128');

//Subscribe to the Redis channel for real time bitcoin data update
sub.subscribe('chat');
sub.subscribe('trades');
sub.subscribe('asks');
sub.subscribe('bids');

function handler (req, res) {
  fs.readFile(__dirname + '/index.html',
  function (err, data) {
    if (err) {
      res.writeHead(500);
      return res.end('Error loading index.html');
    }

    res.writeHead(200);
    res.end(data);
  });
}

io.sockets.on('connection', function (socket) {
	//Grab message from Redis and send to client
    sub.on('message', function(channel, message){
		console.log(channel+' received redis message');
		//console.log(message);
        //socket.send(message);		
		if (channel =='chat'){
			io.sockets.emit('news', message);
		} else if (channel=='trades'){
		    io.sockets.emit('trades', message);
		} else if (channel=='asks'){
		    io.sockets.emit('asks', message);
		} else if (channel=='bids'){
		    io.sockets.emit('bids', message);
		}		
    });
});