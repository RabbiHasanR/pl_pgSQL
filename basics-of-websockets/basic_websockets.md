websockets is a bidirectional communication protocol

http 1.0: use tcp protocol. client always open connection for  request to server and server return response to client then client imidieate close the connections. every time client opent connection and after get response from server close connection in http 1.0 imideatly. this is stateless because after request response client and server no one know about anyone

http 1.1: use tcp protocol. client open connection for request to server and server return response to client then client can again request to server without closing connection. in http1.1 use header keep-alive..in http1.1 client need to request to server. client can close connection but like 1.0 connection does not close imideatly. this is stateless because after request response client and server no one know about anyone


websockets: websockets use tcp and its a statefull  beacause client know about server and server know about client when connection open and websocket handshake. and client or server anyone can send data between them real time using websockets. after handshake websockets become binary protocol.


websokets handshake ws:// or wss://:  first client open connection and http1.1 get request with upgrade header to server then server response with 101 status code  that server say to client i switching protocols. and switch to binary protocols..then websockets connection establish now  client and server can communicate between real time. and thats basically can websokets handshake.  now websockets use http2.0 basicaly its same with this websockets handsakes.

handshake example:
client:

GET /chat HTTP/1.1
Host: server.example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: x3JJhlkfdjaoroewhr==....
Sec-WebSocket-Protocol: chat, superchat
Sec-WebSocket-Version: 13
Origin: http://example.com


Server:

HTTP/1.1 101 Switching Protocols
Upgrade: Websocket
Connection: Upgrade
Sec-WebSocket-Accept: HSmrc0jflsahflsafjl=..
Sec-WebSocket-Protocol: chat

http2.0: 


websockets use cases:
1. chatting
2. live feed
3. multiplayer gaming
4. showing client progress/logging


websockets pros and cons:

pros:

* Full-duplex (no polling)
* HTTP compatible 
* Firewall friendly (standard)

cons:

* Proxying is tricky
* L7 load balancing challenging (timeouts)
* stateful protocol, difficult to horizontally scale

do you have to use websockets?

what really happens during a websockets connection? show based on wiresharking
1. first client handshaking with SYN using tcp protocol to server
2. then server SYN, ACK (ackonowledge) to client
3. then client ACK to server
4. then client get request using http/1.1 to server
5. then server ACK to client
6. then server use HTTP/1.1 protocol to client for Switching protocols
7. client ACK to server
8. then server Ping to client using websocket protocols
9. then client ACK to server
10. client Pong to server using websocket protocols
11. server ACK


now websocket connections is open and client and server can comunnication between them real time


how websockets work with http/2? explain details

http/1 create multiple tcp connections but http/2 create one tcp connection and in this one tcp connection every get, post or websockets request connect each as a stream.



Why WebSockets over HTTP/2 is critical for effective load balancing and backend scalling? explain details


how can i securing websockets and scalling webscokets?

envoy proxy has fearute which not in haproxy:

1. use http/2 with 1 tcp connection with multiple websockets connections
2. dynamic endpoint loading
3. if new envoy process and old envoy process running in different container envoy support hot restart


most of the browser still now usage http/1.1 upgrade..so from browser over http/2 using envoy and websockets backend 1 tcp connection with multiplexing not possible but logical multiplexing possible with 1 tcp connection.


but custom client with go, rust, node.js   to envoy to websockets backend using go, rust, caddy  can use http/2 with 1 tcp connection with real multiplx

ajax vs websocket

short pooling vs long pooling vs sse vs websocket


Django Channel:

channel set up in django project:
pip install channel
add in installed_apps = ['channel']
asgi.py file config:

ProtocolTypeRouter = it works for maping incomming protocl if protocol is http then pass to http request api or protocol is websocket then use for websocket code


in settings.py :
ASGI_APPLICATION = 'project_name.asgi.application'


Consumers: A consumer is the basic unit of channels code. consumers are like django views
tow type consumers: SyncConsumer and AsyncConsumer. A consumer is a subclass of either SyncConsumer or AsyncConsumer.
SyncConsumer will run code synchronously in a threadpool.

sync cousumer create:

from channels.consumer import SyncConsumer

class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print('websocket connect. this method is call when client initially opens a connection and is about to finsh the websocket handshake.')
    
    def websocket_receive(self, event):
        print('websocket recive. this handler is called when data received from client')

    def websocket_disconnect(self, event):
        print('websocket is disconet. this handler is called when either connection to the client is lost, either from the client clossing the connection, the server closing the connection , or loss of the socket.')


AsyncConsumer will expect you to write async capable code.
    from channels.consumer import AsyncConsumer

    class MyAsyncConsumer(AsyncConsumer):

        async def websocket_connect(self, event):
            print('websocket connect. this method is call when client initially opens a connection and is about to finsh the websocket handshake.')
        
        async def websocket_receive(self, event):
            print('websocket recive. this handler is called when data received from client')

        async def websocket_disconnect(self, event):
            print('websocket is disconet. this handler is called when either connection to the client is lost, either from the client clossing the connection, the server closing the connection , or loss of the socket.')



Routing: when we routing consumers we call the as_asgi() classmethod. this returns an asgi wrapper application that will instantiate a new consumer instance for each connection or scope. this is smiller to django as_view(), which plays the same role for per request instance of class bassed views.

Events:

connect-receive event: Sent to the application when the client initialy opens a connection and is about to finish the websocket handshake.
"type": "websocket.connect"

accept-send event: sent by the application when it wishes to accept an incoming connection.
"type": "websocket.send"
"subprotocol":None
"headers": [name, value] where name is header name and value is header value.

receive-receive event: sent to the application when a data message is received from the client
"type":"websocket.receive"
"bytes": None. the message content, if it was binary mode or none. optional if missing it is equivalent to None.
"text": None. the message content. if it was text mode or none. optional if missing it is equivalent to None.


send-send event
sent by the application to send a data message to the client.
"type":"websocket.send"
"bytes": None. the binary message content. if it was bianry mode or none. optional if missing it is equivalent to None.
"text": None. the message content. if it was text mode or none. optional if missing it is equivalent to None.

disconnect-receive event: sent to the application when either connection to the client is lost, either from the client closing the connection, the server closing the connection or loss of the socket.
"type: "websocket.disconnect"
"code": the websocket close code in int, as per the websocket spec.

close-send event: sent by the application to tell the server to close the connection.
"type": "websocket.close"
"code": the websocket close code in int, as per the websocket spec. optional if missing defaults to 1000
"reason": "no need" a reason given for the closure can be any string  optional if missing or nonw deafult is empty string


difference betwwen sync and async consumers:

in sync consumer suppose 1 client connect with websocket and application send data to client 1 but for sending data to client 1 may take some time..at this time any other client can not connect with this sync consumer..also suppose 2 client connected in sync consumer and application sending data to client 1 may take some time in this time application can not sending data to client 2..when sending data to client 1 is finished then sending data to client 2 is starting in sync consumer..

but in async consumer multiple client can connect same time and receive and sending data to multiple clients possible at the same time.

in django channel when we send data client to server or server to cient we send data as string.


Channel layers:  channel layers allow you to talk between different instance of an application. it is high level application to application communication. A channel layer is the transport mechanism that allows multiple consumer instance to communicate with each other an other part of djano. they arre a usefull part  of making a distributed real time application if you don't want to have shuttle all of your messages or events through a database. for channel layer impliment we can use: redis channel layer , in memory channel layer

channels:

groups: 

messages: 

Redis channel layer: redis works as the communication store for the channel layer. in order to use redis as a channel layer you have to install channel_redis package

get_channel_layer()- this functiion is used to get deafult channel layer from a project. from channel.layers import get_channel_layer

channel_layer- this attribute is used to get default channel layer from a project. this contains a pointer to the channel layer instance only if you are using consumers.

channel_name- this attribute contains the channel name that will reach the consumer.

send():this function takes two arguments, the channel to send on, as a unicode string and the message to send as a serializer dict.

group_send(): this function takes two positional arguments, the group to send tto as a unicode string, and the message to send as a serializer dict. it may raise messagetoolarge but  cannot raise channelfull.

group_add(): this  is used to add a channel to a new or existing group.

group_discard(): this is used to remove channel from the group.



Use Database with django channel: this django orm is a synchronous piece of code and so if you want to access it from asynchronous code you need to do special handling to make sure its connections are closed properly. when you are writing asynchronous code or async consumers you will need to call database methods in a safe, synchronous context, using database_sync_to_async

Authentication: AuthMiddleware requires SessionMiddleware to function, which itself requires CookieMiddleware. For convenience these are also provided as a combined callable calles AuthMiddlewareStack that includes all three.

from channel.auth import AuthMiddlewareStack

application = ProtocolTypeRouter(
    {
        'http': get_asgi_application(),
        'websocket': AuthMiddlewareStack (
            URLRouter(
                app.routing.websocket_urlpatterns
            )
        )
    }
)

To access the user, just use self.scope["user"] in you consumer


Generic Consumer: django chaannel generic consumers are: WebsocketConsumer, AsyncWebsocketConsumer, JsonWebsocketConsumer and AsyncJsonWebsocketConsumer

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer, JsonWebsocketConsumer, AsyncJsonWebsocketConsumer

common methods  of WebsocketConsumer, AsyncWebsocketConsumer generic consumer: connect(self), receive(self, test_data=None, bytes_data=None), disconnect(self, close_code)
accept() - this is used to  accept the connection
accept("subprotocol") - this is used to accept the connection and specify a chosen subprotocol

close() - this is used to reject the connection
close(code=4123) - this is used to reject connection with custom websocket error code.

send(text_data="string") - this is used to send data to client
send(bytes_data=data) - this is used to send binary frame to client


common methods  of JsonWebsocketConsumer, AsyncJsonWebsocketConsumer generic consumer: connect(self), receive_json(self, content, **kwargs), disconnect(self, close_code), accept(), close(), send_json(content)


websocket vulnerabilities and prevention techinques:

Dos attacks

No authentication during handshake process

unencrypted tcp channels

vulnerability to input data attacks

data masking

lake of websocket authorization and authentication

tunneling

sniffing attacks

