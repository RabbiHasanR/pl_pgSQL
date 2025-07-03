# Network Performance Concepts

## ⚙️ 1. Bandwidth — Maximum capacity
### 🔍 What is it?
Bandwidth is the maximum amount of data that can be transferred per second over a network connection.

Think of it as the width of a highway — the wider the road, the more cars can travel side-by-side.

### 📏 Measured In:
- Mbps (Megabits per second)
- Gbps (Gigabits per second)

### 💡 Example (Backend):
If your server has 1 Gbps bandwidth, that means up to 125 MB/s of data can be transferred (1 byte = 8 bits).

But remember: Bandwidth is just the maximum potential, not the actual speed.

## ⚙️ 2. Throughput — Actual performance
### 🔍 What is it?
Throughput is the actual amount of data transferred per second, considering real-world conditions (like congestion, server load, etc).

It’s the number of cars that actually pass on the highway per second, not the theoretical max.

### 📏 Measured In:
Same as bandwidth — Mbps or Gbps

### 💡 Example (Backend):
Your server has 1 Gbps bandwidth, but if you’re transferring files and only getting 400 Mbps, then your throughput = 400 Mbps (maybe due to DB bottleneck or TCP retries).

## ⚙️ 3. Latency — Delay or waiting time
### 🔍 What is it?
Latency is the time it takes for data to travel from source to destination — usually measured as Round Trip Time (RTT).

Like the time it takes for a message to reach and come back.

### 📏 Measured In:
Milliseconds (ms)

### 💡 Example (Backend):
If your frontend client in Tokyo calls a backend server in New York:

- Ping time might be 200 ms

That’s latency: how long it takes for a request to reach the server and come back.

## 🧠 Real-World Analogy (Download Water Example)
| Concept   | Analogy                     | Network Example                 |
|-----------|-----------------------------|---------------------------------|
| Bandwidth | Size of the pipe            | Max 100 Mbps internet line      |
| Throughput| Water actually flowing      | Getting 40 Mbps download        |
| Latency   | Delay before water starts   | 150ms delay before loading API  |

## 🧪 Backend-Specific Examples
### ✅ File Download:
- **Bandwidth** = 100 Mbps line
- **Throughput** = 85 Mbps actual download rate
- **Latency** = 50ms from client to server

### ✅ API Call:
Fast backend, but:
- **High latency (200ms)** → because server is far away
- **Low throughput** → client has slow 3G connection

### ✅ Streaming Logs:
You need high throughput and low latency

If latency is too high, real-time logs feel delayed

## 🔥 Why Backend Engineers Must Understand These:
| Impact Area           | How It Affects You                                      |
|-----------------------|---------------------------------------------------------|
| API Performance       | High latency = slow UX even if logic is fast            |
| File Upload/Download  | Throughput affects time to complete                     |
| Microservices         | Internal API calls across services = latency-sensitive  |
| Database Replication  | Bandwidth needed for syncing large volumes             |
| Monitoring & Alerts   | Delay in logs or metrics = delayed insight             |

## 🛠️ Tools to Measure:
| Metric     | Tool                          |
|------------|-------------------------------|
| Bandwidth  | speedtest, iperf              |
| Throughput | iperf, system metrics         |
| Latency    | ping, traceroute, curl -w "%{time_total}" |

## ✅ Summary Table
| Metric     | Description                        | Measured In | Keyword Analogy           |
|------------|------------------------------------|-------------|---------------------------|
| Bandwidth  | Max data capacity                  | Mbps        | Highway width             |
| Throughput | Actual data being transferred      | Mbps        | Cars passing per second   |
| Latency    | Delay before/while sending data    | ms          | Time to start flow        |






# Understanding APIs and REST APIs

## ✅ What is an API?
API stands for Application Programming Interface.

### 📦 Definition:
It is a set of rules and protocols that allows different software systems or components to communicate with each other.

### 🧠 Analogy:
Think of an API like a restaurant menu.  
You (the frontend) choose a dish (send a request) → the kitchen (backend) prepares it → and the waiter (API) delivers it to you.

### ✅ Real-World Example:
Suppose you use a weather app on your phone:  
- The app sends a request to a Weather API like `GET /weather?city=London`  
- The Weather API (hosted by the backend) responds with JSON:

```json
{
  "temperature": "27°C",
  "condition": "Sunny"
}
```

## ✅ What is a REST API?
REST stands for Representational State Transfer.  
It’s a design pattern for building APIs using HTTP and resource-based structure.

### 🧠 Core Concepts of REST:
- **Resources**: Everything is treated as a resource (e.g., users, posts, products)
- **HTTP Verbs**:
  - **GET**: Fetch a resource
  - **POST**: Create a new resource
  - **PUT/PATCH**: Update a resource
  - **DELETE**: Delete a resource
- **Stateless**: Every request from the client must contain all the info needed.
- **Uniform Interface**: Same rules for all resources (use URIs).

## ✅ What is a RESTful API?
RESTful API is simply an API that follows the REST principles.

So:
- **REST API**: refers to the architectural concept.
- **RESTful API**: refers to an API implementation that actually follows the REST rules.

👉 Many people use "REST API" and "RESTful API" interchangeably.

## ✅ RESTful API Example (Blog App)
Suppose you have a blog app with posts.

### Endpoints:
| Operation       | HTTP Method | URL          | Description              |
|-----------------|-------------|--------------|--------------------------|
| Get all posts   | GET         | /posts/      | List all blog posts      |
| Get one post    | GET         | /posts/5/    | Get post with ID 5       |
| Create new post | POST        | /posts/      | Add a new blog post      |
| Update post     | PUT/PATCH   | /posts/5/    | Edit post with ID 5      |
| Delete post     | DELETE      | /posts/5/    | Delete post with ID 5    |

### Sample Response (GET /posts/5/):
```json
{
  "id": 5,
  "title": "What is REST?",
  "content": "REST is a set of principles...",
  "author": "Rabbi"
}
```

## ✅ Trade-offs of RESTful API
### ✅ Advantages:
| Advantage       | Explanation                                                  |
|-----------------|--------------------------------------------------------------|
| 🌍 Stateless     | Scales easily since server doesn’t store client state.       |
| 🔁 Cacheable    | Responses can be cached to improve speed.                    |
| 📏 Standardized  | Easy to understand and follow (common HTTP methods).         |
| 🔧 Flexible      | Works with any frontend (React, mobile, etc.)                |

### ❌ Disadvantages:
| Disadvantage       | Explanation                                                  |
|--------------------|--------------------------------------------------------------|
| 📦 Over-fetching   | You might get more data than needed (GET /users returns too much). |
| 🔁 Multiple requests | Nested resources often need extra API calls.                |
| 📚 Too generic     | REST doesn’t define how to handle versioning, filtering, sorting, etc. |
| 🚦 No real-time    | REST is request/response; doesn’t support push like WebSockets. |

## ✅ When to Use REST APIs
Use REST APIs when:
- You need a clean, simple, stateless interface.
- Your system is CRUD-heavy (e.g., e-commerce, blogs, admin dashboards).
- You want broad compatibility with frontend/mobile frameworks.






# Understanding Scaling

🔍 **What is Scaling?**  
Scaling is the process of increasing your system's capacity to handle more users, more requests, or more data.

There are two main types:  
- **Vertical Scaling (Scale Up)**  
- **Horizontal Scaling (Scale Out)**  

## 1️⃣ Vertical Scaling (Scaling Up)
### 📦 Definition:
Increasing the resources (CPU, RAM, SSD, etc.) of a single server.

### 🧠 Analogy:
Upgrading your laptop from 8 GB RAM to 32 GB RAM so it runs faster.

### ✅ Example:
Suppose you run a web server on a VM with:  
- 2 CPUs  
- 4 GB RAM  

Now you upgrade to:  
- 8 CPUs  
- 32 GB RAM  

The server can now handle more users without changing your code or infrastructure.

### ✅ Pros:
| Advantage                          | Explanation                                                  |
|------------------------------------|--------------------------------------------------------------|
| ✅ Simple to implement              | No code/config changes needed. Just upgrade hardware.         |
| ✅ No distributed system complexity | No need to manage multiple servers.                          |
| ✅ Lower latency                    | Everything runs on one machine (no network hops).             |

### ❌ Cons:
| Disadvantage                      | Explanation                                                  |
|-----------------------------------|--------------------------------------------------------------|
| ❌ Expensive                       | High-end hardware gets costly quickly.                       |
| ❌ Single Point of Failure         | If the server dies, everything goes down.                    |
| ❌ Limited ceiling                 | You can only upgrade hardware to a point (you'll eventually hit a limit). |
| ❌ Downtime required               | Often need to restart to scale up.                           |

## 2️⃣ Horizontal Scaling (Scaling Out)
### 📦 Definition:
Adding more servers/nodes to your system to share the load.

### 🧠 Analogy:
Instead of hiring one superhuman to do everything, you hire 5 normal people to divide the work.

### ✅ Example:
Suppose you have one web server running a Django app. Now traffic increases.  

You add:  
- 3 more servers (so total 4)  
- Use a load balancer (like Nginx, HAProxy




# Understanding Load Balancers

## 🧭 What is a Load Balancer?
### ✅ Definition:
A load balancer is a system (hardware or software) that distributes incoming network traffic across multiple servers (backend nodes) to:  
- Improve performance  
- Avoid overloading any single server  
- Ensure high availability  

### 🧠 Analogy:
Imagine you’re at a busy restaurant. There’s a receptionist (load balancer) who assigns customers to available tables (servers) so no waiter gets overwhelmed.

### 🔧 Load Balancer Working Flow
```
Client → Load Balancer → Multiple Servers
```

**Example:**
```
Client → Load Balancer → [Server A, Server B, Server C]
```
The load balancer chooses the best server based on a balancing algorithm.

## 🧱 Types of Load Balancer
| Type                     | Description                                                  |
|--------------------------|--------------------------------------------------------------|
| 🧠 Software Load Balancer | Runs on Linux/macOS/Windows as a service (e.g., Nginx, HAProxy) |
| 🧱 Hardware Load Balancer | Physical devices (e.g., F5, Cisco) used in data centers       |
| ☁️ Cloud Load Balancer   | Managed service by cloud providers (AWS ELB, GCP Load Balancer, Azure ALB) |

## ⚖️ Types by Layer
| Layer   | Type                   | Description                                                  |
|---------|------------------------|--------------------------------------------------------------|
| Layer 4 | Transport Layer LB     | Balances TCP/UDP traffic (e.g., IP + Port)                   |
| Layer 7 | Application Layer LB   | Makes decisions based on HTTP headers, URLs, cookies, etc. (e.g., route /api/ to API server) |

## 🧠 6 Most Common Load Balancing Algorithms
### 1️⃣ Round Robin
**🎯 What:**  
Distributes requests one-by-one to servers in a circular order.

**⚙️ Example:**  
- Request 1 → Server A  
- Request 2 → Server B  
- Request 3 → Server C  
- Request 4 → Server A  
...

**✅ Pros:**  
- Simple  
- Works well when all servers are equal in capacity  

**❌ Cons:**  
- Doesn't consider server load or response time  

### 2️⃣ Weighted Round Robin
**🎯 What:**  
Same as Round Robin, but gives more traffic to more powerful servers.

**⚙️ Example:**  
- Server A: weight 2  
- Server B: weight 1  
- Requests → A, A, B, A, A, B...  

**✅ Pros:**  
- Better for heterogeneous servers  
- Easy to configure  

**❌ Cons:**  
- Doesn't adapt dynamically to real-time load  

### 3️⃣ Least Connections
**🎯 What:**  
Sends traffic to the server with the fewest active connections.

**✅ Pros:**  
- Great when sessions/requests are long-lived  
- Efficient for real-time apps  

**❌ Cons:**  
- Slight overhead in tracking connection count  
- Doesn’t consider server response time  

### 4️⃣ Weighted Least Connections
**🎯 What:**  
Like Least Connections, but uses server weights to prefer stronger machines.

**✅ Pros:**  
- Balances long sessions more intelligently  
- Works well with mixed-capacity servers  

**❌ Cons:**  
- More complex to configure  

### 5️⃣ IP Hash (Source IP Affinity)
**🎯 What:**  
Uses the client's IP address to always route the same client to the same server.

**⚙ 금융 Example:**  
- User from IP 192.168.1.2 → always goes to Server A  
- Sticky sessions behavior.

**✅ Pros:**  
- Good for session persistence  
- Reduces cache invalidation  

**❌ Cons:**  
- Uneven traffic distribution  
- Can break if IP address changes (mobile users)  

### 6️⃣ Least Response Time
**🎯 What:**  
Chooses the server with the fastest current response time.

**✅ Pros:**  
- Ideal for low-latency apps  
- Adapts to real-time performance  

**❌ Cons:**  
- Needs performance monitoring  
- May require additional software or custom logic  

## 🆕 1️⃣ Sticky Round Robin
**🎯 What is it?**  
Sticky Round Robin (also called Session-Aware Round Robin) is a hybrid:  
- It combines Round Robin with session persistence ("stickiness").  
- Once a client is assigned to a server, all future requests from that client go to the same server, until a timeout or logout.

**🧠 Example:**  
You have 3 servers: A, B, and C  

| Request | Client IP     | Assigned Server        |
|---------|---------------|------------------------|
| 1       | 192.168.1.2   | A (via Round Robin)    |
| 2       | 192.168.1.3   | B                      |
| 3       | 192.168.1.2   | A (Sticky: same as before) |
| 4       | 192.168.1.4   | C                      |

**✅ Pros:**  
| Advantage                     | Explanation                                                  |
|-------------------------------|--------------------------------------------------------------|
| ✅ Maintains session state     | Good for login, shopping carts, etc.                         |
| ✅ Balanced over time          | Still distributes new sessions fairly                        |

**❌ Cons:**  
| Disadvantage                  | Explanation                                                  |
|-------------------------------|--------------------------------------------------------------|
| ❌ May cause imbalance         | If too many clients "stick" to the same server               |
| ❌ Session tracking needed     | Usually via cookies, tokens, or IP address                   |
| ❌ Not scalable alone         | Needs backup handling if a server goes down                  |

## 🧪 Real-Life Load Balancer Examples
| Tool / Service      | Type                  | Description                               |
|---------------------|-----------------------|-------------------------------------------|
| 🧰 Nginx            | Software (Layer 7)    | Reverse proxy and load balancer           |
| 🧰 HAProxy          | Software (Layer 4/7)  | High performance TCP/HTTP LB              |
| ☁️ AWS ELB         | Cloud LB (L4/L7)      | Elastic Load Balancer                     |
| ☁️ Google Cloud LB | Cloud LB (L4/L7)      | Global load balancing                     |
| ⚙️ Envoy Proxy      | Modern proxy          | Advanced LB + observability               |
| 🧱 F5 BIG-IP        | Hardware (Enterprise) | Enterprise-grade LB device                |

## 📊 Comparison Table of Algorithms
| Algorithm              | Traffic Awareness       | Server Health         | Session Stickiness | Use Case Example           |
|------------------------|-------------------------|-----------------------|--------------------|---------------------------|
| Round Robin            | ❌ Equal only           | ❌ No                 | ❌ No              | Simple app with equal servers |
| Weighted Round Robin   | ✅ Weighted             | ❌ No                 | ❌ No              | Mixed servers             |
| Least Connections      | ✅ Yes                  | ❌ No                 | ❌ No              | Chat apps, video streaming |
| Weighted Least Conn    | ✅ Yes + weights        | ❌ No                 | ❌ No              | Microservices with variance |
| IP Hash                | ❌ No                  | ❌ No                 | ✅ Yes             | Login sessions, carts     |
| Least Response Time    | ✅ Fastest wins         | ✅ Needs monitor       | ❌ No              | Low-latency APIs          |

## 🏁 Summary
| Concept               | Vertical Scaling       | Horizontal Scaling                          |
|-----------------------|------------------------|---------------------------------------------|
| Load Balancer Role    | Not needed             | Essential to distribute load                |

## 🔚 Final Thoughts
Load balancers are critical in any production-grade distributed system.  

Choosing the right algorithm depends on:  
- **Server types** (homogeneous vs heterogeneous)  
- **Type of traffic** (short requests vs long sessions)  
- **Performance needs** (latency vs throughput)  

You can often combine multiple strategies (e.g., weighted + least connections).



# Understanding API Gateways

## 🚪 What is an API Gateway?
An API Gateway is a reverse proxy that sits between your client (frontend/mobile) and backend services (microservices, monoliths, etc.). It acts as a single entry point that handles:

- Routing requests to the right service
- Security (JWT validation, OAuth, API keys)
- Rate limiting
- Logging & monitoring
- Load balancing
- Request transformation

**Think of it as the traffic controller for all your APIs.**

## 🧱 Why Use an API Gateway?
**Without a gateway**, clients must:
- Call each microservice directly
- Handle security, retries, discovery, etc.
- Be tightly coupled to backend structure

**With a gateway**:
- One consistent entry point (e.g., `api.yourapp.com`)
- Internal services are hidden and protected
- Centralized security, analytics, throttling

## 🛠️ Core Features of API Gateways
| Feature             | Description                                                  |
|---------------------|--------------------------------------------------------------|
| **Routing**         | Route `/api/users` to user-service, `/api/orders` to order-service |
| **Authentication**  | Validate JWTs, OAuth2 tokens, API keys                       |
| **Rate Limiting**   | Protect backend from abuse (e.g., 100 req/min per IP)        |
| **Caching**         | Cache GET responses to reduce load                           |
| **Load Balancing**  | Distribute traffic across multiple instances                 |
| **Request Rewriting**| Modify headers, paths, or payloads                           |
| **Monitoring**      | Access logs, latency, status codes                          |
| **CORS Handling**   | Allow frontend domains to access APIs                        |

## ⚙️ Common API Gateway Software
You have two main categories: **open-source (self-hosted)** and **managed (cloud-based)**.

### ✅ 1. Open Source / Self-Hosted Gateways
These are tools you run yourself — in Docker, Kubernetes, or on VMs.

#### 🔹 Kong
- Built on NGINX + Lua
- Plugin-based architecture
- Has both OSS and Enterprise versions
- Supports JWT, rate limiting, logging, transformations
- Admin API for dynamic configuration
- **➡️ Good for**: medium to large production systems with plugin needs
- **🔗** https://konghq.com

#### 🔹 NGINX
- Powerful reverse proxy and load balancer
- Can be configured as API gateway
- Supports JWT validation via Lua or third-party modules
- Extremely performant
- **➡️ Good for**: low-level control, performance-focused apps
- **🔗** https://nginx.org

#### 🔹 Traefik
- Modern, cloud-native, dynamic gateway
- Auto-discovers services in Docker/Kubernetes
- Built-in support for TLS, Let's Encrypt
- Lightweight and easy to deploy
- **➡️ Good for**: containerized environments
- **🔗** https://traefik.io

#### 🔹 Envoy
- High-performance proxy created by Lyft
- Used in Istio and modern service mesh stacks
- Full support for observability, retries, timeouts
- Complex config but very powerful
- **➡️ Good for**: service mesh / enterprise-grade setups
- **🔗** https://www.envoyproxy.io

#### 🔹 KrakenD
- API gateway focused on performance
- Combines and filters multiple backend responses
- Low-latency, easy to configure JSON-based system
- **➡️ Good for**: API aggregation or BFF (Backend for Frontend)
- **🔗** https://www.krakend.io

### ✅ 2. Managed API Gateways (Cloud Providers)
These are fully managed, no-infrastructure gateways — you configure via UI or CLI.

#### ☁️ AWS API Gateway
- Supports REST and WebSocket APIs
- Integrates with Lambda, ECS, IAM
- Built-in JWT/OAuth2 validation
- Throttling, logging, and WAF support
- **🔗** https://aws.amazon.com/api-gateway/

#### ☁️ Google Cloud API Gateway / Apigee
- Secure and manage APIs at scale
- Apigee supports API monetization, policy control
- Great analytics
- **🔗** https://cloud.google.com/api-gateway  
- **🔗** https://cloud.google.com/apigee

#### ☁️ Azure API Management
- Full API lifecycle management
- Supports policies, quotas, CORS, OpenAPI
- Integration with Azure Active Directory
- **🔗** https://azure.microsoft.com/en-us/products/api-management/

#### ☁️ Cloudflare API Gateway
- Built-in WAF, DDoS protection
- Extremely fast at edge locations
- Rules-based routing
- **🔗** https://developers.cloudflare.com/api-shield/

## 📌 When Should You Use an API Gateway?
**Use one if you**:
- Have microservices architecture
- Need centralized security & throttling
- Expose public APIs
- Support multiple clients (web, mobile, IoT)

**You might skip it if**:
- You’re building a monolith
- Everything is internal and low-scale