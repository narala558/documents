var port = process.env.PORT || 8008
  , server = require('http').createServer()
  , io = require('socket.io')(server)
// , redis = require('redis')
  , socketIORedis = require('socket.io-redis')
  , redisPort = 6379
  , redisHost = 'pubsub-redis.pubsub'
  , redis = require('redis').createClient
  , pub = redis(redisPort, redisHost, { auth_pass: process.env.REDIS_PASSWORD })
  , sub = redis(redisPort, redisHost, { auth_pass: process.env.REDIS_PASSWORD })
  , adapter = socketIORedis({ pubClient: pub, subClient: sub })

io.adapter(adapter);

io.on('connection', function (socket) {

  socket.on('subscribe', function(data) {
    socket.join(data.room);
    console.log("User joined the room: ", data);
  })

  socket.on('unsubscribe', function(data) {
    socket.leave(data.room);
    console.log("User left the room: ", data);
  })

  socket.on('disconnect', function(data) {
    socket.leave(data.room);
    console.log("User quit the room: ", data);
  })

});

adapter.subClient.on("message", function (channel, message) {

  console.log("New Message in Channel: %s", channel);
  if (channel == "notify") {
    data = JSON.parse(message);
    data.rooms.forEach(function(room){
      io.in(room).emit(data.event, data.data);
    });

    console.log("new message: ", message);
  }

});


adapter.subClient.subscribe("notify");

console.log('server listens on port ' + port);
server.listen(port);
