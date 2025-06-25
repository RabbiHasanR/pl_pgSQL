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