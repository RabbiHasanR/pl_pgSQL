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



