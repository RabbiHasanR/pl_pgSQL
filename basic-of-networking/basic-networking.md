# 🧠💡 When You Type a URL — The Secret Journey Behind the Scenes

Ever wondered what *really* happens when you type `www.example.com` and hit Enter?  
Let’s uncover the magic — step by step — with fun names and deeper explanations.

---

## 🛜 1. 🌐 Name Seeker (DNS) — Finding the Real Address

Imagine trying to call a friend named "Google" — but your phone needs the actual number, not just the name. That’s what **DNS** (Domain Name System) does.

- You type `google.com`, your computer asks DNS:  
  *“What number (IP address) should I call?”*
- DNS replies:  
  *“Here it is: `142.250.190.78`”*

This is like a global contact list for websites. Without it, the internet would be total chaos.

🔑 **Why it matters**:  
DNS lets humans use easy-to-remember names, while computers use real IP addresses to connect.

---

## 🏠 2. 📫 Digital Address Book (IP & Port) — Finding the Right Door

Once your computer knows the IP, it still needs to know *which door* to knock on.

- **IP Address**: Like the building address.
- **Port Number**: Like the specific room or department.

**Example**:  
`142.250.190.78:443` → Go to Google, knock on the HTTPS room (port 443).

🔑 **Why it matters**:  
Ports help servers run multiple services. One server can serve web pages (port 80/443), emails (port 25), files (port 21), and more — all from the same IP!

---

## 🧾 3. 📡 Data Courier (TCP/UDP) — Choosing the Delivery Style

Now you know *where* to send data. But *how* should it be sent? There are two delivery methods:

- **TCP (Talk Carefully Protocol)**: Delivers messages with care. Double-checks if everything arrived. Perfect for websites, payments, and logins.
- **UDP (Ultra Direct Protocol)**: Delivers fast, doesn’t wait for feedback. Ideal for games, video calls, and live streams.

🔑 **Why it matters**:  
Use TCP when accuracy is critical, UDP when speed matters more than perfection.

---

## 🤝 4. 📞 Connection Greeter (TCP Handshake) — Setting Up the Call

Before chatting, your computer and the server say hello to ensure the connection is clear. This is the **TCP 3-way handshake**:

1. You: *“Hi! Can we talk?”* (SYN)
2. Server: *“Sure, I hear you!”* (SYN-ACK)
3. You: *“Awesome, let’s begin!”* (ACK)

🔑 **Why it matters**:  
This ensures both sides are listening and ready before data starts flowing. It’s polite — and secure!

---

## 🌍 5. 📥 The Real Conversation (HTTP/HTTPS) — Asking for What You Need

With the connection established, you make your real request:  
*“Please give me the blog post with ID 5.”*

This happens using:

- **HTTP**: Normal request.
- **HTTPS**: Secure, encrypted request.

🔑 **Why it matters**:  
This is where your frontend meets the backend. Everything from loading a webpage to submitting a form happens here.

---

## 🔐 6. 🕵️ Secret Keeper (SSL/TLS) — Protecting the Chat

Without **SSL/TLS**, anyone in the middle (like hackers or shady Wi-Fi networks) can read your message. With SSL/TLS, the message becomes a secret code that only your browser and the server can decode.

🔑 **Why it matters**:  
It keeps passwords, credit cards, and personal info safe from prying eyes.

---

## 🚦 7. 🧠 Smart Gatekeeper (Load Balancer & Reverse Proxy) — Managing Traffic

If a million people visit a website at once, a single server would panic! That’s where these come in:

- **Load Balancer**: Spreads visitors across multiple servers.
- **Reverse Proxy**: Hides and protects backend servers while smartly routing requests.

🔑 **Why it matters**:  
This keeps your website fast, stable, and secure — even during heavy traffic.

---

## 🛡️ 8. 🚫 Digital Bodyguard (Firewall) — Blocking the Bad Guys

The **firewall** checks every visitor and asks:  
*“Are you safe?”*

If the visitor is harmful — *boom* 💥 — blocked. It stops:

- Hackers
- Unauthorized access
- Suspicious activity

🔑 **Why it matters**:  
A strong firewall keeps your backend and data safe from threats and attacks.

---

## ✅ 🚀 Full Journey Recap

```plaintext
You (Browser)
 ↓
🌐 Name Seeker (DNS)
 ↓
📫 Digital Address (IP + Port)
 ↓
📡 Data Courier (TCP/UDP)
 ↓
🤝 Connection Greeter (TCP Handshake)
 ↓
🔐 Secret Keeper (SSL/TLS)
 ↓
📥 Real Conversation (HTTP Request)
 ↓
🧠 Smart Gatekeeper (Proxy/Load Balancer)
 ↓
🛡️ Digital Bodyguard (Firewall)
 ↓
🎉 Server Response
```

---

This journey happens in milliseconds, bringing the web to your screen with speed, security, and precision. Next time you type a URL, you’ll know the *secret sauce* behind the scenes! 🚀





# What is DNS?

DNS (Domain Name System) is like the phonebook of the internet.  
It translates human-readable domain names (like www.google.com) into IP addresses (like 142.250.190.68) that computers use to identify each other.

Without DNS, you’d have to remember IP addresses of every website — which is impractical.

## 📞 Real-World Analogy
You want to call “Pizza Hut”, but your phone only works with phone numbers, not names. So you check a phonebook to get the number for “Pizza Hut”.

Same for computers:  
You type www.google.com → your computer asks DNS → DNS replies with an IP like 142.250.190.68.

## 🔁 DNS Lookup: Step-by-Step Breakdown
When you type www.example.com in your browser, here's what happens under the hood:

### ✅ Step 1: Check Local Cache
Your OS/browser first checks if it has already resolved this domain recently.

If found, DNS query ends here (saves time).

### ✅ Step 2: Ask the Recursive Resolver (usually your ISP or system DNS)
If not cached, your system sends a DNS query to a recursive resolver (e.g., 8.8.8.8 for Google DNS).

This resolver will do the work of finding the IP on your behalf.

### ✅ Step 3: Ask the Root DNS Server
Recursive resolver asks one of the 13 root DNS servers (like a.root-servers.net).

Root server doesn’t know the exact IP but responds with:

“I don’t know www.example.com, but ask the .com TLD server.”

### ✅ Step 4: Ask the TLD DNS Server
The resolver then queries the TLD (Top-Level Domain) server (like .com, .org, .net, etc.)

.com server replies:

“I don’t know www.example.com's IP, but the name server for example.com is ns1.exampledns.com.”

### ✅ Step 5: Ask the Authoritative Name Server
The resolver now asks the authoritative DNS server (e.g., ns1.exampledns.com):

“What is the IP for www.example.com?”

This server knows the final answer and replies with the IP:

93.184.216.34

### ✅ Step 6: Send IP Back to Client
The resolver caches the IP for future use and returns it to your computer.

Your browser now sends an HTTP request to 93.184.216.34, and the site loads.

## 📊 Diagram Summary:
```
You ⟶ Resolver ⟶ Root ⟶ TLD (.com) ⟶ Authoritative DNS ⟶ IP returned ⟶ You
```

## 🧠 How Does DNS Handle Billions of Domains?
DNS uses a distributed and hierarchical system — that's the secret.

### Key Points:
**Distributed:**

- No single server holds all domain mappings.
- Each zone (like .com, .org, or google.com) has its own authoritative DNS servers.

**Hierarchical:**

- Starts from root (.), then TLD (.com), then domain (google.com), then subdomain (www.google.com).
- Makes lookup fast and scalable.

**Caching:**

- Resolvers cache results to avoid repeating lookups.
- Browsers, OS, and DNS providers (like Cloudflare or Google DNS) maintain these caches.

**TTL (Time To Live):**

- Each DNS record has a TTL — tells how long to cache.
- Reduces load on DNS servers.

## 🧱 Types of DNS Servers
| Type                  | Role                                                                 |
|-----------------------|----------------------------------------------------------------------|
| Recursive Resolver    | Does the full lookup process for the client (e.g., 8.8.8.8, 1.1.1.1) |
| Root Server           | Top of DNS hierarchy (13 logical servers)                            |
| TLD Server            | Manages domains like .com, .org, .bd                                 |
| Authoritative Server   | Has the actual IP for the domain (e.g., ns1.cloudflare.com)          |

## 🌐 Popular Public DNS Resolvers
| Provider      | IP Address              |
|---------------|-------------------------|
| Google DNS    | 8.8.8.8, 8.8.4.4       |
| Cloudflare    | 1.1.1.1, 1.0.0.1       |
| OpenDNS       | 208.67.222.222         |

## 🛡️ DNS Security (Bonus)
- **DNS Spoofing / Poisoning:** Attacker gives fake DNS response.
- **DNSSEC:** Adds cryptographic signatures to ensure authenticity of DNS data.
- **DoH/DoT:** DNS over HTTPS/TLS to encrypt DNS queries.

## ✅ Summary
| Concept               | Meaning                                              |
|-----------------------|------------------------------------------------------|
| DNS                   | Maps domain names to IP addresses                    |
| Root Server           | Knows where TLD servers are                         |
| TLD Server            | Knows where domain's DNS is                         |
| Authoritative Server   | Knows exact IP of a domain                          |
| Recursive Resolver     | Does the full lookup and caching                    |
| Caching               | Makes lookups fast and efficient                    |
| TTL                   | Time duration to cache a DNS record                 |








# Networking and OSI Model — A Beginner-Friendly Guide with Real-Life Examples

This guide explains how hosts communicate over networks and breaks down the **OSI (Open Systems Interconnection) Model** with simple analogies and examples. It’s designed to make networking concepts accessible for beginners while providing practical insights for building reliable, efficient systems.

## Table of Contents
- [What Is a Host?](#what-is-a-host)
- [IP Address: Every Host Needs an Identity](#ip-address-every-host-needs-an-identity)
- [Subnetting: Hierarchical IP Assignment](#subnetting-hierarchical-ip-assignment)
- [What Is a Network?](#what-is-a-network)
- [Basic Networking Devices](#basic-networking-devices)
- [OSI Model: The 7 Layers of Networking](#osi-model-the-7-layers-of-networking)
- [Encapsulation and Decapsulation](#encapsulation-and-decapsulation)
- [Bonus: How IP and MAC Work Together (ARP)](#bonus-how-ip-and-mac-work-together-arp)
- [Switching vs Routing](#switching-vs-routing)
- [Final Thoughts](#final-thoughts)

## What Is a Host?
A **host** is any device that sends or receives data over a network. Examples include:
- Computers, laptops, phones, tablets
- Printers, servers (physical or cloud)
- Smart devices (TVs, fridges, thermostats, smartwatches)

If it connects and communicates over a network, it’s a host.

### Types of Hosts
- **Clients**: Initiate requests (e.g., opening a website).
- **Servers**: Respond to requests (e.g., delivering a webpage).

## IP Address: Every Host Needs an Identity
Each host is assigned an **IP address**, like a postal address, to identify where to send data.

- **IPv4**: 32-bit address in four octets (e.g., `192.168.1.5`).
  - Each octet ranges from 0 to 255.
  - Example: 
    ```
    Binary: 10001000.00010110.00010001.01100010
    Decimal: 136.22.17.98
    ```

# Public IP vs Private IP and Port Forwarding

This guide explains the differences between **public IP** and **private IP** addresses, how they work together to enable internet communication, and the role of **port forwarding** in exposing internal devices to the outside world.

## Table of Contents
- [What Is a Public IP?](#what-is-a-public-ip)
- [What Is a Private IP?](#what-is-a-private-ip)
- [How Do Devices with Private IP Access the Internet?](#how-do-devices-with-private-ip-access-the-internet)
- [What Is Port Forwarding?](#what-is-port-forwarding)
- [Quick Summary](#quick-summary)
- [Use Case Examples](#use-case-examples)

## What Is a Public IP?
A **public IP address** is assigned to your router or modem by your Internet Service Provider (ISP). It’s the address visible to the internet, allowing external communication.

### Analogy
Think of a public IP as the street address of an apartment building. Anyone outside (e.g., Amazon delivery, friends) uses it to find the building.

### Example
- Your home network might have a public IP like `203.0.113.42`.
- Search "What is my IP?" on Google to see your public IP.
- Only one device (usually your router) gets this public IP.
- All internal devices (laptop, phone, smart TV) share this IP when accessing the internet.

## What Is a Private IP?
A **private IP address** is assigned by your router to devices within your local network (e.g., phone, PC, smart TV). These addresses are not routable on the public internet and are used only within your local network.

### Analogy
If the public IP is your building’s street address, private IPs are like apartment numbers inside that building.

### Example
- Your laptop: `192.168.0.101`
- Your phone: `192.168.0.102`
- Your printer: `192.168.0.150`
- These devices can communicate internally but cannot be reached directly from outside unless configured.

### Common Private IP Ranges
- `10.0.0.0 – 10.255.255.255`
- `172.16.0.0 – 172.31.255.255`
- `192.168.0.0 – 192.168.255.255`

## How Do Devices with Private IP Access the Internet?
Devices with private IPs use **NAT (Network Address Translation)** to access the internet. The router:
- Replaces the private IP with the public IP for outgoing requests.
- Tracks which internal device sent each request using ports.
- Returns responses to the correct device.

**Example**: When your phone accesses `google.com`, the router sends the request using the public IP and tracks the response to deliver it back to your phone.

## What Is Port Forwarding?
**Port forwarding** allows external devices to access a specific device inside your private network via the public IP.

### Why Use It?
To access a private device (e.g., server, camera, game console) from outside your network.

### Real-World Example
You run a web server on your laptop at home (private IP: `192.168.0.101`, port 80). To access it externally:
- Set up port forwarding in your router:
  ```
  External Port 80 → Forward to 192.168.0.101:80
  ```
- External users visit `http://203.0.113.42`, and the router forwards the request to your laptop’s port 80.

**Flow**:
```
http://203.0.113.42 → (Router sees port 80 → Forwards to 192.168.0.101:80)
```

### Security Consideration
Port forwarding exposes internal devices to the internet, so:
- Only forward necessary ports.
- Use firewalls, authentication, and VPNs.
- Avoid forwarding ports to insecure services (e.g., old cameras, unpatched software).

## Quick Summary
| Concept        | Public IP                     | Private IP                    |
|----------------|-------------------------------|-------------------------------|
| **Scope**      | Global (Internet-wide)        | Local (within home/office)    |
| **Assigned by**| ISP                           | Your Router (via DHCP)        |
| **Uniqueness** | Must be unique on the internet| Must be unique only in LAN    |
| **Example**    | `203.0.113.42`               | `192.168.0.101`              |

| Concept        | Port Forwarding               |
|----------------|-------------------------------|
| **Purpose**    | Allow external access to a private host |
| **Setup On**   | Router (using admin interface) |
| **Example**    | External Port 80 → Internal IP:80 |

## Use Case Examples
| Use Case                     | Public IP Needed | Port Forwarding Required |
|------------------------------|------------------|--------------------------|
| Browsing Google              | ✅               | ❌                       |
| Hosting Game Server at Home  | ✅               | ✅                       |
| Accessing CCTV remotely      | ✅               | ✅                       |
| Printing at Home             | ❌ (local only)  | ❌ (unless remote access) |
| Accessing NAS remotely       | ✅               | ✅ (or better, use VPN)   |



## Subnetting: Hierarchical IP Assignment
Organizations use subnetting to structure IP addresses for better device management.

**Example: ACME Inc.**
```yaml
Head Office: 10.x.x.x

Branches:
- New York: 10.20.x.x
- London:   10.30.x.x
- Tokyo:    10.40.x.x

Departments:
- Sales:        10.20.55.x
- Engineering:  10.20.66.x
- Marketing:    10.20.77.x
```
IP `10.30.55.127` refers to a host in:
- ACME Inc. → London branch → Sales department

## What Is a Network?
A **network** is a group of interconnected hosts that can communicate. Examples:
- **Home Wi-Fi**: Devices on the same router.
- **Office LAN**: Computers, printers, etc.
- **Subnets**: Subdivided networks (like classrooms in a school).
- **The Internet**: A global network of networks.

## Basic Networking Devices
- **Repeater**: Extends signals over long distances by regenerating weak signals.
- **Hub**: Multi-port repeater; broadcasts all traffic to all connected hosts (inefficient, insecure).
- **Bridge**: Connects hubs, filters traffic, and forwards data only to the necessary side.
- **Switch**: Smart hub; sends data directly to the destination host using port mappings.
- **Router**: Connects different networks, maintains a routing table, and directs data between networks or to the internet.

## OSI Model: The 7 Layers of Networking
The **OSI Model** divides network communication into 7 layers, each with a specific role:
1. Physical
2. Data Link
3. Network
4. Transport
5. Session
6. Presentation
7. Application

### Real-Life Analogy: Sending a Letter
Imagine Host A sending a letter to Host B. Each OSI layer adds its own "envelope" and "label" to the data.

#### 7. Application Layer (Your App)
- Where you write a message in WhatsApp or type a URL in a browser.
- **Protocols**: HTTP, FTP, DNS.

#### 6. Presentation Layer (Translator)
- Translates data (text, audio, video) into a format both devices understand.
- Handles encryption/decryption and data compression.

#### 5. Session Layer (Conversation Tracker)
- Manages and tracks sessions (who is talking to whom).

#### 4. Transport Layer (Post Office Sorting Room)
- Breaks data into segments and adds port numbers to identify services.
- Uses **TCP** (reliable) or **UDP** (faster, less reliable).
- **Example**: Web browsers use port 80 (HTTP), video calls use port 5004 (RTP/UDP).

#### 3. Network Layer (Mail Carrier Between Cities)
- Adds source and destination IP addresses.
- Finds the best route to the destination.
- **Protocol**: IP (Internet Protocol).

#### 2. Data Link Layer (Local Delivery Truck)
- Adds source and destination MAC addresses.
- Handles hop-to-hop delivery within a local network.
- **Protocol**: Ethernet.

#### 1. Physical Layer (The Road)
- Transmits raw bits (1s and 0s) over cables, fiber, or Wi-Fi.
- **Devices**: Cables, NICs, switches, wireless radios.

## Encapsulation and Decapsulation
### Sending Data (Encapsulation)
Each layer adds a header to the data:
```yaml
Layer 7-5: Your message
⬇️
Layer 4: + Port Info (TCP/UDP header)
⬇️
Layer 3: + IP Info
⬇️
Layer 2: + MAC Info
⬇️
Layer 1: 010101010101... (sent as bits)
```

### Receiving Data (Decapsulation)
The receiver reverses the process:
```yaml
Layer 1: Receive bits
⬆️
Layer 2: Extract MAC info
⬆️
Layer 3: Extract IP info
⬆️
Layer 4: Extract Port info
⬆️
Layer 7-5: Rebuild the message for the application
```

## Bonus: How IP and MAC Work Together (ARP)
When Host A sends data to Host B:
- Host A knows Host B’s IP address but needs its MAC address.
- Uses **ARP (Address Resolution Protocol)** to map the IP to a MAC address.
- Enables Layer 2 communication within the local network.

## Switching vs Routing
| Feature         | Switching                     | Routing                       |
|-----------------|-------------------------------|-------------------------------|
| **Layer**       | Layer 2 (Data Link)           | Layer 3 (Network)             |
| **Devices**     | Switch                        | Router                        |
| **Works Within**| Same network                  | Different networks            |
| **Uses**        | MAC address                   | IP address                    |
| **Example**     | Communication inside office   | Communication between offices via internet |

## Final Thoughts
Understanding networking — from physical cables to IP routing — is the foundation of modern internet systems. The **OSI Model** provides a structured way to visualize and troubleshoot data movement across networks. The next time you send a message or load a webpage, remember the 7-layer system making it all possible.







# TCP vs UDP — Deep Dive for Backend and Network Engineers

This guide provides a comprehensive breakdown of **TCP** (Transmission Control Protocol) and **UDP** (User Datagram Protocol), their mechanics, pros, cons, use cases, and trade-offs. Understanding these transport protocols is essential for backend and network engineers designing performant, scalable, and secure systems.

## Table of Contents
- [What Is TCP?](#what-is-tcp)
- [What Is UDP?](#what-is-udp)
- [How TCP Works](#how-tcp-works)
- [How UDP Works](#how-udp-works)
- [Comparison Table](#comparison-table)
- [Use Cases](#use-cases)
- [Final Thoughts](#final-thoughts)

## What Is TCP?
**TCP** (Transmission Control Protocol) is a **connection-oriented**, reliable transport protocol used for web browsing, email, SSH, and database traffic. It ensures data is delivered accurately and in order.

### Pros
- **Acknowledgment (ACKs)**: Ensures data receipt with ACKs; retransmits if no ACK is received.
- **Guaranteed Delivery**: Automatically retransmits lost or dropped packets.
- **Connection-Based**: Establishes a reliable session via a 3-way handshake:
  ```
  Client → SYN
  Server → SYN-ACK
  Client → ACK
  ```
- **Congestion Control**: Adjusts transmission speed to avoid network congestion using algorithms like slow start.
- **Ordered Packets**: Numbers segments to ensure data is reassembled in the correct order.

### Cons
- **Larger Packets**: Adds headers (sequence numbers, ACKs, flags), increasing packet size (20–60 bytes).
- **More Bandwidth Overhead**: ACKs, retransmissions, and control flags consume bandwidth.
- **Slower Than UDP**: Handshake, congestion control, and guarantees add latency.
- **Stateful Protocol**: Tracks connection state, increasing complexity and memory usage.
- **Server Memory = DoS Risk**: Open connections (e.g., SYN flood) can exhaust server memory.

## What Is UDP?
**UDP** (User Datagram Protocol) is a **connectionless**, lightweight transport protocol that prioritizes speed over reliability. It’s used for real-time applications like streaming and gaming.

### Pros
- **Smaller Packets**: Minimal headers (8 bytes) reduce overhead.
- **Less Bandwidth**: No handshakes, ACKs, or retransmissions.
- **Faster Than TCP**: No setup or ACK delays, ideal for real-time applications.
- **Stateless**: No connection state, reducing server memory usage.

### Cons
- **No Acknowledgement**: No confirmation of data receipt; lost packets are gone.
- **No Guaranteed Delivery**: Best-effort delivery with no retransmissions.
- **Connectionless**: No handshake or session awareness.
- **No Congestion Control**: Can flood networks, leading to packet loss.
- **No Ordered Packets**: Applications must handle out-of-order packets.
- **Security Risk**: Easier to spoof packets; used in DDoS amplification attacks (e.g., DNS, NTP).

## How TCP Works
### TCP 3-Way Handshake
```
1. Client: SYN → (I want to connect)
2. Server: SYN-ACK → (I accept)
3. Client: ACK → (Let’s go)
```
### Data Flow
- Segments data into packets.
- Adds sequence numbers.
- Sends packets and waits for ACKs.
- Retransmits if ACKs are not received.
### Connection Close
- Uses a 4-way FIN/ACK teardown to close connections.

## How UDP Works
### No Handshake
- Client sends datagrams without setup or ACKs.
- No session tracking.
### One-Shot Packets
- Each packet is independent.
- Applications must handle loss or retries.

## Comparison Table
| Feature                | TCP                            | UDP                            |
|------------------------|--------------------------------|--------------------------------|
| **Reliable Delivery**  | ✅ Yes (ACKs, retries)        | ❌ No                          |
| **Ordered Packets**    | ✅ Yes                        | ❌ No                          |
| **Congestion Control** | ✅ Yes                        | ❌ No                          |
| **Latency**            | 🐢 Slower                    | ⚡ Faster                      |
| **Header Size**        | Larger (20–60 bytes)          | Small (8 bytes)                |
| **Protocol Type**      | Stateful, connection-oriented | Stateless, connectionless      |
| **Best For**           | Web, email, databases         | Streaming, gaming, VoIP        |
| **Packet Loss Handling**| Automatic retransmit          | Application-level (manual)     |
| **Setup Time**         | 3-way handshake               | None                           |
| **Security**           | More protected                | Easier to spoof                |

## Use Cases
### TCP
- Web browsing (HTTP/HTTPS)
- Email (SMTP, IMAP, POP3)
- Database connections (PostgreSQL, MySQL)
- SSH, FTP
- File transfers

### UDP
- Video streaming (e.g., YouTube, Twitch)
- VoIP calls (Zoom, Skype)
- Online gaming (e.g., multiplayer shooters)
- DNS queries
- DHCP (IP assignment)
- Real-time telemetry or sensor data

## Final Thoughts
- **Use TCP** for applications requiring reliability, ordered delivery, and complete data transfer, such as web applications or database queries.
- **Use UDP** for speed-critical applications that can tolerate some packet loss, like video streaming, gaming, or telemetry.
- Understanding TCP and UDP mechanics empowers backend engineers to optimize performance, scalability, and security in network-dependent systems.





# 🚀 Evolution of HTTP: From HTTP/1.0 to HTTP/1.1 to HTTP/2 — Explained with Visuals

The HyperText Transfer Protocol (HTTP) is the foundation of communication on the web. From its humble beginnings in HTTP/1.0 to the powerful and fast HTTP/2, the protocol has evolved significantly to meet the demands of modern websites and applications.

In this document, we’ll break down:

- How HTTP/1.0, HTTP/1.1, and HTTP/2 work under the hood
- How they use TCP connections
- Key differences between them
- Why HTTP/2 is a game-changer

Let’s dive in 🚀

## 🧱 1. HTTP/1.0 — The Original Web Protocol

### 🔧 How It Works:
- Introduced in 1996 (RFC 1945)
- Each HTTP request opens a new TCP connection
- The connection closes after a single response

### 🧠 Key Features:
- Stateless protocol
- No support for persistent connections
- No support for request pipelining or multiplexing

### 🔄 Workflow Diagram:
```
1. Open TCP connection
2. Send HTTP request
3. Receive HTTP response
4. Close TCP connection
```

### 🧨 Problem:
Every image, CSS, or JS file on a webpage requires a new TCP connection. This creates latency and inefficiency.

## 🔁 2. HTTP/1.1 — Smarter, But Still Sequential

### 🔧 How It Works:
- Introduced in 1999 (RFC 2616)
- Uses a persistent TCP connection by default (keep-alive)
- Allows multiple requests over the same connection
- Requests are still served sequentially

### 🧠 Key Improvements:
- Persistent connections
- Chunked transfer encoding
- Host header for virtual hosting
- Optional pipelining (but not widely used due to complexity)

### 🔄 Workflow Diagram:
```
1. Open TCP connection
2. Send Request A
3. Receive Response A
4. Send Request B
5. Receive Response B
6. ...
7. Close TCP (or keep alive)
```

### 🔸 Still has a problem:
Responses must come back in order, causing Head-of-Line Blocking at the HTTP layer.

## 🧵 3. HTTP/2 — Fully Multiplexed and Binary-Powered

### 🔧 How It Works:
- Introduced in 2015 (RFC 7540)
- Uses one TCP connection
- Supports multiplexing: multiple streams over the same connection
- Transmits data in binary frames

### 🧠 Key Features:
- True parallelism: Multiple requests/responses sent at the same time
- Header compression (HPACK)
- Prioritization and stream dependency
- Efficient use of TCP bandwidth

### 🔄 Visual Workflow:
```
One TCP connection:
 ┌────────────┐
 │ Stream #1  │── Request A ─▶
 │ Stream #2  │── Request B ─▶
 │ Stream #2  │◀─ Response B
 │ Stream #1  │◀─ Response A
 └────────────┘
```
*Responses can come back out of order, eliminating blocking at the HTTP level.*

## 🔍 Summary Comparison Table

| Feature                     | HTTP/1.0                     | HTTP/1.1                             | HTTP/2                          |
|-----------------------------|------------------------------|--------------------------------------|---------------------------------|
| **TCP Connection per Request** | ✅ Yes                      | ❌ No (keep-alive by default)         | ❌ No (always single TCP)        |
| **Persistent Connection Support** | ❌ No                   | ✅ Yes                               | ✅ Yes                          |
| **Request Multiplexing**     | ❌ No                       | ❌ No                                | ✅ Yes                         |
| **Head-of-Line Blocking**    | 🔥 Severe                  | ⚠️ Present at HTTP layer             | ✅ Eliminated at HTTP level     |
| **Binary Framing**           | ❌ No                       | ❌ No                                | ✅ Yes                         |
| **Header Compression**       | ❌ No                       | ❌ No                                | ✅ HPACK                        |
| **Pipelining**               | ❌ No                       | ⚠️ Optional (but unsafe)             | ✅ Handled via streams          |

## 🎨 Visual Evolution Summary

### HTTP/1.0
```
[Request 1] → [Response 1]
(close connection)
[Request 2] → [Response 2]
(close connection)
```

### HTTP/1.1 (Keep-Alive)
```
[Request 1] → [Response 1]
[Request 2] → [Response 2]
(connection stays open)
```

### HTTP/2 (Multiplexed)
```
[Stream A: Req/Resp]
[Stream B: Req/Resp]
[Stream C: Req/Resp]
(all interleaved in same TCP pipe)
```

## 🧠 Final Thoughts

HTTP has come a long way:

- **HTTP/1.0**: Simple, but slow due to one request per TCP connection.
- **HTTP/1.1**: Improved efficiency with keep-alive but still sequential.
- **HTTP/2**: Revolutionized performance with multiplexed streams, compression, and binary framing.







# 🔐 SSL vs TLS — The Secure Backbone of the Web, Explained for Backend Engineers

If you’re building APIs, securing services, or managing infrastructure, TLS (Transport Layer Security) is a critical component of your stack. This document demystifies SSL and TLS, explains their handshake mechanics, and provides practical insights for backend engineers.

In this guide, we’ll cover:
- The difference between SSL and TLS
- How HTTP (stateless) works over TCP (stateful)
- TLS 1.2 vs. TLS 1.3 handshake mechanics
- How symmetric keys are securely established
- Pros, cons, and real-world implications for backend development

---

## 🌐 SSL vs TLS — What’s the Difference?

**SSL (Secure Sockets Layer)** was the original protocol for securing web traffic, pioneered by Netscape in the 1990s. However, SSL has significant vulnerabilities:
- **SSL 2.0** (1995): Insecure due to weak ciphers and protocol flaws.
- **SSL 3.0** (1996): Vulnerable to attacks like POODLE, making it obsolete.

**TLS (Transport Layer Security)** is the modern successor, designed to address SSL’s flaws:
- **TLS 1.0** (1999): Incremental improvement over SSL 3.0, now deprecated.
- **TLS 1.1** (2006): Added protections, also deprecated.
- **TLS 1.2** (2008): Widely used, supports modern ciphers but slower.
- **TLS 1.3** (2018): Current standard, faster and more secure.

> **Note**: When people refer to “SSL certificates,” they mean certificates used with TLS. SSL is entirely deprecated and should not be used.

---

## 🧠 How Does HTTP (Stateless) Work Over TCP (Stateful)?

- **TCP**: A stateful protocol that establishes a reliable, ordered connection between client and server.
- **HTTP**: A stateless protocol where each request-response pair is independent.

**How it works together**:
- TCP provides the transport layer, managing connection state and ensuring reliable data delivery.
- HTTP operates at the application layer, sending stateless requests and responses over the TCP connection.
- With TLS, HTTP traffic is encrypted and transported over a secure TCP channel, adding confidentiality and integrity.

---

## 🤝 TLS 1.2 Handshake — Step-by-Step (with ECDHE)

TLS 1.2 is still common in production environments. The handshake establishes a secure session using **Elliptic Curve Diffie-Hellman Ephemeral (ECDHE)** for key exchange.

### 🔄 Handshake Flow:
1. **Client Hello**:
   - Client sends supported cipher suites, a random nonce, and ECDHE curve preferences.
2. **Server Hello**:
   - Server responds with chosen cipher suite, its certificate (containing public key), a random nonce, and its ECDHE public key.
3. **Client Key Generation**:
   - Client generates its own ephemeral ECDHE key pair (private and public keys).
   - Computes the **shared secret** using:
     ```
     shared_secret = ECDHE(client_private_key, server_public_key)
     ```
4. **Master Secret Derivation**:
   - Both client and server derive a master secret using a Pseudo-Random Function (PRF):
     ```
     master_secret = PRF(shared_secret, client_random, server_random)
     ```
5. **Symmetric Key Derivation**:
   - Symmetric encryption keys (e.g., AES) are derived from the master secret for encrypting application data.
6. **Finished Messages**:
   - Both sides send encrypted “Finished” messages to verify the handshake and key agreement.

> **Key Points**:
> - Only public keys are exchanged; private keys never leave their respective sides.
> - Requires **2 round-trips (2-RTT)** before application data can be sent.
> - Supports legacy RSA key exchange (now deprecated) and ECDHE for forward secrecy.

---

## 🧵 TLS 1.3 Handshake — Faster, Simpler, and More Secure

TLS 1.3, standardized in 2018 (RFC 8446), is designed for speed and security, reducing latency and removing outdated cryptography.

### 🔄 Handshake Flow:
1. **Client Hello**:
   - Client sends cipher suites, its ECDHE public key, and a random nonce.
2. **Server Hello**:
   - Server responds with its certificate, ECDHE public key, random nonce, and encrypted extensions.
3. **Shared Key Derivation**:
   - Both sides compute the **shared secret**:
     ```
     shared_secret = ECDHE(private_key, peer_public_key)
     ```
   - Use the **HKDF (HMAC-based Key Derivation Function)** to derive encryption keys.
4. **Encrypted Finished**:
   - Both sides send “Finished” messages encrypted with the derived symmetric keys.

### ✅ Key Differences from TLS 1.2:
- **1-RTT** for initial connections; **0-RTT** for resumed sessions using Pre-Shared Keys (PSK).
- Only supports **ECDHE** for key exchange (RSA key exchange removed).
- Removes deprecated algorithms (e.g., SHA-1, MD5).
- Encrypts more handshake metadata, including Server Name Indication (SNI).
- Prevents downgrade attacks by hiding protocol version and cipher suite choices.

---

## 📊 TLS 1.2 vs TLS 1.3 — Comparison Table

| Feature                   | TLS 1.2                           | TLS 1.3                           |
|---------------------------|-----------------------------------|-----------------------------------|
| **Handshake Round Trips**  | 2 RTT                            | 1 RTT (0 RTT for resumption)     |
| **Key Exchange**          | ECDHE, RSA (deprecated)          | ECDHE only                       |
| **Forward Secrecy**       | Optional                         | ✅ Enforced                      |
| **Deprecated Algorithms** | Supports RSA, SHA-1, MD5         | 🚫 All removed                   |
| **Metadata Encryption**   | ❌ No                            | ✅ Yes (e.g., SNI)               |
| **Session Resumption**    | Session ID or tickets            | Pre-Shared Key (PSK)             |
| **Performance**           | Slower (more round-trips)        | ✅ Faster (fewer round-trips)    |

---

## ✅ Why TLS 1.3 Is More Secure (and Faster)

1. **Enforced Forward Secrecy**:
   - Every session uses ephemeral keys, ensuring that even if a server’s private key is compromised, past sessions remain secure.
2. **Simplified Design**:
   - Removes legacy features, reducing attack surface (e.g., no support for weak ciphers like RC4).
3. **Prevents Downgrade Attacks**:
   - Encrypts handshake metadata to prevent attackers from forcing weaker protocol versions.
4. **Reduced Latency**:
   - Fewer round-trips mean faster page loads and API responses, critical for performance-sensitive applications.

---

## 🧠 Real-World Impact for Backend Engineers

1. **Adopt TLS 1.3**:
   - Most modern servers (Nginx, Apache, Cloudflare, AWS ALB) support TLS 1.3. Enable it for better security and performance.
2. **Configure Secure Cipher Suites**:
   - For TLS 1.2, use ECDHE-based ciphers (e.g., `ECDHE-RSA-AES256-GCM-SHA384`) and disable RSA key exchange.
   - Example Nginx configuration:
     ```
     ssl_protocols TLSv1.2 TLSv1.3;
     ssl_ciphers ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384;
     ssl_prefer_server_ciphers on;
     ```
3. **Debugging TLS Issues**:
   - Use tools like `openssl s_client` or Wireshark to inspect handshake failures.
   - Common issues: Mismatched cipher suites, expired certificates, or incorrect SNI.
4. **Certificate Management**:
   - Use Let’s Encrypt or AWS Certificate Manager for automated renewals.
   - Ensure certificates include the full chain (root + intermediate) to avoid trust issues.
5. **Mutual TLS (mTLS)**:
   - For secure microservices, implement mTLS to authenticate both client and server.
6. **Avoid Common Pitfalls**:
   - Don’t use self-signed certificates in production.
   - Disable SSL 2.0/3.0 and TLS 1.0/1.1 to prevent attacks like DROWN or BEAST.

---

## 🔚 Final Thoughts

TLS is the invisible shield protecting billions of transactions, API calls, and user interactions daily. As a backend engineer, understanding TLS handshakes, cipher suites, and certificate management is critical for building secure, high-performance systems.

- **Prioritize TLS 1.3** for speed and security.
- **Audit configurations** to eliminate weak ciphers and protocols.
- **Stay vigilant** about certificate renewals and handshake debugging.

By mastering TLS, you ensure trust, confidentiality, and integrity for your applications.





# Proxy vs Reverse Proxy — Explained

This guide provides a clear and concise explanation of **proxies** and **reverse proxies**, their differences, use cases, practical examples, trade-offs, and bottlenecks. Whether you're building secure systems, managing traffic across microservices, or deploying scalable APIs, understanding these tools is essential for backend engineers.

## Table of Contents
- [What Is a Proxy Server?](#what-is-a-proxy-server)
- [What Is a Reverse Proxy?](#what-is-a-reverse-proxy)
- [Key Differences](#key-differences)
- [Use Cases](#use-cases)
- [Real-World Examples](#real-world-examples)
- [Trade-offs and Bottlenecks](#trade-offs-and-bottlenecks)
- [Frequently Asked Questions (FAQ)](#frequently-asked-questions-faq)
- [Final Thoughts](#final-thoughts)

## What Is a Proxy Server?
A **proxy server** acts as an intermediary between a client and the internet (target server). When a user requests a resource (e.g., visiting `google.com`), the request goes through the proxy, which forwards it to the destination and returns the response to the client.

**Flow**:
```
Client → Proxy → Target Server (e.g., google.com)
       ↩ Response ↩
```

From the target server's perspective, the request originates from the proxy, not the client.

### Use Cases for a Proxy
- **Caching**: Stores responses to reduce bandwidth and improve response times.
- **Anonymity/Privacy**: Masks the client’s IP address.
- **Logging and Monitoring**: Tracks and audits user requests.
- **Access Control**: Blocks specific domains (e.g., social media) for productivity or security.
- **Internal Routing**: Manages traffic between secure zones or networks.

## What Is a Reverse Proxy?
A **reverse proxy** sits in front of backend servers, receiving client requests and forwarding them to the appropriate internal server. Clients interact only with the reverse proxy (e.g., `api.company.com`), unaware of the backend infrastructure.

**Flow**:
```
Client → Reverse Proxy → Server 1 / Server 2 / Server 3
```

**Examples**: Nginx, HAProxy, Envoy, Pingora (Cloudflare).

### Use Cases for a Reverse Proxy
- **Load Balancing**: Distributes traffic across multiple servers based on health, weight, or round-robin.
- **Caching Static Assets**: Stores pages, images, or files for faster delivery (CDN-style).
- **SSL Termination**: Handles HTTPS at the edge, forwarding plain HTTP internally.
- **Routing & URL Rewriting**: Directs requests to specific services (e.g., `/api/v1` to one service, `/admin` to another).
- **Canary Deployments & A/B Testing**: Routes a percentage of traffic to new service versions.
- **Microservices Gateway**: Acts as an API gateway for multiple internal microservices.

## Key Differences
| Feature            | Proxy                          | Reverse Proxy                     |
|--------------------|--------------------------------|-----------------------------------|
| **Client Knows**   | Final destination (e.g., google.com) | Only the proxy (e.g., nginx)      |
| **Server Sees**    | Only the proxy's IP           | Only the proxy's IP               |
| **Purpose**        | Client → Internet             | Internet → Server(s)              |
| **Example Use**    | Browsing anonymously          | Load balancing, microservices     |
| **Who Uses It?**   | End-users or networks         | API servers, infrastructure teams |

## Real-World Examples
### Proxy for Blocking and Logging
In enterprises:
- All internet traffic routes through an internal proxy firewall.
- The firewall:
  - Logs traffic to monitor malicious behavior.
  - Blocks risky domains (e.g., social media).
  - Caches static content (e.g., fonts, scripts from CDNs).

### Nginx as a Reverse Proxy
```nginx
server {
    listen 80;
    server_name api.myapp.com;

    location / {
        proxy_pass http://backend1.internal;
    }
}
```
This configuration hides the backend server’s real IP, exposing only `api.myapp.com` to clients.

## Trade-offs and Bottlenecks

### Proxy
**Benefits**:
- **Anonymity & Privacy**: Masks client identity from the target server.
- **Content Caching**: Reduces bandwidth and improves response time.
- **Access Control**: Filters or blocklists for traffic management.
- **Traffic Monitoring**: Centralized logging and audit trails.
- **Bypass Restrictions**: Circumvents geographic or network limitations.

**Trade-offs & Bottlenecks**:
| Issue                     | Explanation                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| **Single Point of Failure**| If the proxy goes down, no internet traffic can pass through.               |
| **Latency Overhead**      | Each request makes an extra hop (Client → Proxy → Target), increasing delay.|
| **No End-to-End Security**| Unless HTTPS is used throughout, the proxy can see/alter requests.         |
| **Scalability Limits**    | A centralized proxy can become a bottleneck if not scaled properly.         |
| **Complex Troubleshooting**| Errors in upstream sites can look like proxy issues to end users.          |
| **Limited Protocol Support**| Some proxies support only HTTP; not suitable for real-time (WebSocket, FTP).|
| **Caching Staleness**     | Cached content might be outdated if cache invalidation isn’t handled well.  |

### Reverse Proxy
**Benefits**:
- **Load Balancing**: Distributes traffic intelligently across multiple backends.
- **SSL Termination**: Handles TLS encryption once, reducing backend overhead.
- **Routing and Rewrite**: Smartly routes traffic to different microservices or paths.
- **Caching**: Improves performance by serving static or semi-static content from the edge.
- **Security Layer**: Hides internal infrastructure and absorbs malicious traffic (DDoS).
- **Zero-Downtime Deployments**: Supports blue/green, canary, and A/B testing setups.

**Trade-offs & Bottlenecks**:
| Issue                     | Explanation                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| **Latency Addition**      | Adds a network hop before reaching the real server.                         |
| **Single Point of Failure**| If the reverse proxy crashes or misroutes traffic, everything goes down.    |
| **Complex Configuration** | Requires precise routing, health checks, timeouts, and header forwarding.   |
| **Encrypted Traffic Debugging**| Harder to troubleshoot TLS issues post-SSL termination.                |
| **Header Manipulation Issues**| Missed or incorrect forwarding headers (e.g., X-Forwarded-For) can break logic.|
| **Load Imbalance Risk**   | If not properly configured, some servers may get overloaded.                |
| **Caching Inconsistency** | If not coordinated, reverse proxy cache can serve outdated or wrong content.|
| **Stateful Sessions**     | Sticky sessions needed for stateful apps unless session storage is external.|

### Example Bottleneck Scenario
For a high-traffic e-commerce site:
- A reverse proxy (e.g., Nginx) handles SSL, load balancing, and routing to backend APIs.
- If Nginx:
  - Isn’t tuned for concurrent connections (e.g., worker limits, buffers),
  - Fails to forward headers like `X-Forwarded-Proto` or `Host`,
  - Or misroutes requests during canary deployment…
- **Result**: The app may fail silently, route traffic to the wrong backend, or drop connections entirely.

### Design Takeaways
- Ensure proxies/reverse proxies are highly available (use failover, load-balanced clusters).
- Monitor health (Nginx, HAProxy, Envoy expose health/status endpoints).
- Use proper timeouts, circuit breakers, and cache control headers.
- Observe bottlenecks using logs, tracing (e.g., Jaeger), or metrics (e.g., Prometheus/Grafana).

## Frequently Asked Questions (FAQ)
### 1. Can proxy and reverse proxy be used together?
Yes. For example:
```
Client → Proxy (e.g., corporate proxy/VPN)
       → Internet → Reverse Proxy (e.g., Nginx)
       → Backend Service
```

### 2. Can a proxy replace a VPN for anonymity?
- **Proxy**: Hides your IP but may not encrypt traffic unless HTTPS is used.
- **VPN**: Encrypts all traffic, including DNS, at the OS level. Safer for public Wi-Fi.
  - **VPN**: Secure tunnel
  - **Proxy**: Traffic redirect

### 3. Is a proxy only for HTTP?
No. Types of proxies include:
- **HTTP Proxy**: For HTTP/S traffic.
- **SOCKS Proxy**: Protocol-agnostic (supports FTP, SMTP, P2P).
- **Transparent Proxy**: Invisible to the user.
- **Forward Proxy**: Client-facing.
- **Reverse Proxy**: Server-facing.
- **CDN Proxy**: Content delivery (e.g., Cloudflare).

## Final Thoughts
Proxies and reverse proxies are critical for modern backend architecture. They enable:
- Scalability (via load balancing)
- Security (via SSL termination and access control)
- Performance (via caching)
- Advanced deployment strategies (e.g., canary, blue/green deployments)

A skilled backend engineer understands the flow of requests from browser to service to database, leveraging proxies and reverse proxies to optimize and secure systems while mitigating their trade-offs and bottlenecks.







# Layer 4 vs Layer 7 Proxy — Deep Dive for Backend Engineers

This guide explains **Layer 4 (L4)** and **Layer 7 (L7)** proxies, their differences, use cases, trade-offs, and practical examples. Understanding these proxy types is critical for building scalable, secure backend systems.

## Table of Contents
- [What Are OSI Layers?](#what-are-osi-layers)
- [What Is a Layer 4 Proxy?](#what-is-a-layer-4-proxy)
- [What Is a Layer 7 Proxy?](#what-is-a-layer-7-proxy)
- [Comparison Table](#comparison-table)
- [Real-World Examples](#real-world-examples)
- [Trade-offs and Bottlenecks](#trade-offs-and-bottlenecks)
- [Which One Should You Use?](#which-one-should-you-use)
- [Final Thoughts](#final-thoughts)

## What Are OSI Layers?
A quick refresher on the OSI model:

| Layer | Name          | Example Protocols     |
|-------|---------------|-----------------------|
| 7     | Application   | HTTP, HTTPS, gRPC     |
| 6     | Presentation  | TLS/SSL               |
| 5     | Session       | RPC, sockets          |
| 4     | Transport     | TCP, UDP              |
| 3     | Network       | IP                    |

## What Is a Layer 4 Proxy?
A **Layer 4 proxy** operates at the **Transport Layer** (TCP/UDP). It forwards raw packets between client and backend without inspecting the content of the application-layer data.

### How It Works
- Operates at TCP/UDP level.
- Forwards packets as soon as the TCP connection is established.
- Acts like a "connection router" (e.g., NGINX/HAProxy in L4 mode).
- Does not inspect HTTP headers, methods, or cookies.

### Key Characteristics
- Proxies based on IP address and port.
- Fast and low-latency.
- Cannot read HTTP method, headers, or cookies.
- Cannot perform intelligent routing or caching.
- Works with any TCP-based protocol (e.g., HTTP, FTP, SMTP, SSH).

### Use Cases
- Database proxying (e.g., MySQL, PostgreSQL TCP routing).
- Load balancing SSH or custom TCP services.
- UDP services like DNS.
- TLS pass-through (SSL termination on backend).

## What Is a Layer 7 Proxy?
A **Layer 7 proxy** operates at the **Application Layer** (HTTP/HTTPS). It understands the content of requests and can make decisions based on the HTTP method, headers, or body.

### How It Works
- Operates at the HTTP level after TCP connection is established.
- Reads the full HTTP request before routing to a backend.
- Can inspect method, headers, body, cookies, etc.
- Often used for reverse proxies and API gateways.

### Key Characteristics
- Content-aware: understands POST, GET, cookies, JWT, etc.
- Routes traffic based on URL path, headers, or method.
- Supports caching, compression, and URL rewriting.
- Slightly higher latency due to request parsing.

### Use Cases
- HTTP API Gateway.
- Content caching/CDNs.
- Smart routing for microservices.
- Load balancing web applications.
- Authentication and rate limiting.

## Comparison Table
| Feature                | Layer 4 Proxy                  | Layer 7 Proxy                  |
|------------------------|--------------------------------|--------------------------------|
| **OSI Layer**          | Transport (TCP/UDP)           | Application (HTTP, HTTPS)      |
| **Protocol Awareness** | ❌ No                         | ✅ Yes                         |
| **Request Parsing**    | ❌ No                         | ✅ Full request + headers       |
| **Speed**              | ⚡ Faster (low overhead)      | 🐢 Slower (due to inspection)   |
| **Flexibility/Routing**| ❌ IP/port only               | ✅ Method, path, header-based   |
| **SSL/TLS Handling**   | ✅ Pass-through               | ✅ Can terminate               |
| **Caching Support**    | ❌ No                         | ✅ Yes                         |
| **Best For**           | TCP load balancing, databases | HTTP apps, API routing, smart logic |

## Real-World Examples
### Layer 4 Proxy: TCP Load Balancer
**Scenario**: Client connects to an NGINX load balancer for a database.
```
Client → [L4 NGINX Proxy] → TCP Connection to Backend Server
```
**NGINX Configuration**:
```nginx
stream {
    upstream backend {
        server 10.0.0.1:3306;
        server 10.0.0.2:3306;
    }

    server {
        listen 3306;
        proxy_pass backend;
    }
}
```
- NGINX immediately opens a TCP connection to the backend and passes packets without inspecting content.

### Layer 7 Proxy: HTTP Reverse Proxy
**Scenario**: Client sends an HTTP request to an NGINX reverse proxy.
```
GET /
