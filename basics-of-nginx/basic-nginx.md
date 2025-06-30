What is Nginx?

nginx is a software which act a web server and proxy both.

web server: serves web content

proxy: Load balancing, comunicate to backend, backend routing, caching

why we need nginx?

suppose client or frontend need to coonect you api server. then how the connect? client can connect with api server using ip:port. for this client must be know about ip:port. now for more traffic we need to another api server. so use this api server client need to know this api server ip:port..so nginx solve this problem with reverse porxy..everytime client hit nginx and nginx know which api server to communicate how..client only need to hit nginx using url rest of the things do nginx..nginx also use for caching, load balancing, server static content.

architecture:
client -> nginx -> api server(can be multiple api server) -> db

Load balancing


Nginx Internal Architecture:


client request -> os kernel -> nginx start multiple worker process based on os cpu core like (worker 1, worker 2, worker 3, worker 4) each worker can server thousands of connections. worker read connection and decide connection need to get static resource or read from upstream backend, need to load balancing between api servers for serves api data. -> api servers 


proxy: suppose you want to go to google.com through proxy myproxy.com..then you first hit to proxy myproxy.com and myproxy.com know where is google.com..googl.com does not know about client..for google.com client is myproxy.com..proxy can use for :
caching - when multiple request from client to googlc.com..then we can use proxy for caching google.com for everytime we don't need to go to google.com
anonymity - google.com does not about actual client..he know about proxy. here proxy work for anonymity
loggin - for loggin request
block sites - use proxy for block sites. suppose  in software company dose not want to visits facebook,youtube or dangerous sites during worktime for their employees..then using proxy can bloks these sites.
microservices: comunicate between microservices can use proxy.

reverse proxy: in proxy server does not about actual client but in reverse proxy client does not about final destination. client only knows web server likes nginx,haproxy,envoy,pingora etc web servers..server knows only final destination. cause only web server knows which server with connect may ber server 1, server 2 or server 3. thats why its call reverse proxy.
use cases of reverse proxy: caching, load balancing, routing, canary deployment, microservices

most common questions about proxy and reverse proxy:
1. can proxy and reverse proxy used in the same time?
    yes. how?

2. can i use proxy insted of vpn for annomity?
    yes. but vpn is more secure than proxy. how?
3. is proxy just for http traffic? 
    no. you can have so many types of proxies. which?


level 4 proxy:
in level 4 proxy similiar to level 7 but there is on emajor difference..when client request to nginx build tcp connection then nginx does not know about request . request type, headers etc and nginx can not wait for recive full requext packets.nginx imidieatly build tcp connection connect with server and start to pass request packets to server..also when server return response to nginx and nginx return response to client same thing happen


level 7 proxy:

suppose client request nginx reverse proxy . this requect build tcp connection to nginx. then i have two api servers. nginx use load balancing and round robin algorithm and connect to server 1 build tcp connection..also another requect nginx can reverse proxy to server 2 and build tcp connection..this is called layer 7  proxy.

in lavel 7 proxy when client request to nginx then nginx must receive full requext packets and nginx can read this request info like request type, headers etc..then when nginx request to server also server must recive full requext packet and server can read this request info like request type, headers etc..
and when return response server to nginx then nginx first recive full response then return to client full response..since nginx or server can know everything about requext then we can do many thing in nginx layer or server layer..like cacing in nginx layer etc


TLS:

SSL:


http1.0:

http1.1:

http2:


