from collections import deque
import heapq

class Edge:
    def __init__(self, src, dest, weight=0):
        self.src = src
        self.dest = dest
        self.weight = weight
        
        
def add_edge(graph, edge):
    graph[edge.src].append(edge)
    
def print_vertex_neighbours(graph, vertex):
    if vertex >= len(graph):
        return
    for edge in graph[vertex]:
        print(f"neighbour:{edge.dest}, weight: {edge.weight}")
        
    print("\n")
    
    
def print_all_vertex_with_neighbours(graph):
    for i in range(len(graph)):
        print(f"Vertex {i} has edges to:", [f"neighbour:{edge.dest}, weight: {edge.weight}" for edge in graph[i]])
    

def bfs(graph):
    q = deque()
    q.append(graph[0][0].src)
    visited = [False] * len(graph)
    while q:
        v = q.popleft()
        if not visited[v]:
            print(v, end=" ")
            visited[v] = True
            for edge in graph[v]:
                q.append(edge.dest)
    print()
    
def dfs(graph, start, visited):
    print(start, end=" ")
    visited[start] = True
    for edge in graph[start]:
        v = edge.dest
        if not visited[v]:
            dfs(graph, v, visited)
            

def printAllPath(graph, start, visited, path, tar):
    visited[start] = True
    if start == tar:
        print(path)
        return
    for edge in graph[start]:
        v = edge.dest
        if not visited[v]:
            # visited[v] = True
            printAllPath(graph, v, visited, path + str(v), tar)
            visited[v] = False
    # visited[start] = False


def create_directed_weighted_graph(v=6):
    
    graph = [[] for _ in range(v)]
       
    add_edge(graph, Edge(0, 1, 2))
    add_edge(graph, Edge(0, 2, 4))
       
    add_edge(graph, Edge(1, 3, 7))
    add_edge(graph, Edge(1, 2, 1))
       
    add_edge(graph, Edge(2, 4, 3))
       
    add_edge(graph, Edge(3, 5, 1))
       
    add_edge(graph, Edge(4, 3, 2))
    add_edge(graph, Edge(4, 5, 5))
       
    return graph
       

def disjkstra(graph, src):
    v = len(graph)
    dist = [float("inf")] * v
    dist[src] = 0
    vis = [False] * v
    pq = []
    
    heapq.heappush(pq, (0, src))
    
    while pq:
        d, n = heapq.heappop(pq)
        if not vis[n]:
            vis[n] = True
            for edge in graph[n]:
                u = edge.src
                v = edge.dest
                
                if dist[u] + edge.weight < dist[v]:
                    dist[v] = dist[u] + edge.weight
                    heapq.heappush(pq, (dist[v], v))
    
    for d in dist:
        print(d, end=" ")
    
    print()
    
    
def create_directed_wighted_graph_for_bellman(v = 5):
    graph = [[] for _ in range(v)]
    
    add_edge(graph, Edge(0, 1, 2))
    add_edge(graph, Edge(0, 2, 4))
    
    add_edge(graph, Edge(1, 2, -4))
    
    add_edge(graph, Edge(2, 3, 2))
    
    add_edge(graph, Edge(3, 4, 4))
    
    add_edge(graph, Edge(4, 1, -1))
    
    return graph

def bellamn_ford(graph, src):
    ver = len(graph)
    dis = [float("inf")] * ver
    dis[src] = 0
    for k in range(ver-1):
        for i in range(ver):
            for edge in graph[i]:
                u = edge.src
                v = edge.dest
                w = edge.weight
                
                if dis[u] != float('inf') and dis[u] + w < dis[v]:
                    dis[v] = dis[u] + w
                    
    # detect negative weight cycle
    for i in range(ver):
        for edge in graph[i]:
            u = edge.src
            v = edge.dest
            w = edge.weight
            
            if dis[u] != float('inf') and dis[u] + w < dis[v]:
                print("negative weight cycle")
    
    for d in dis:
        print(d, end=" ")
    print()
    
def create_undirected_graph(v=4):
    graph = [[] for _ in range(v)]
    add_edge(graph, Edge(0,2,2))
    # add_edge(graph, Edge(1,3,0))
    add_edge(graph, Edge(1,2,10))
    add_edge(graph, Edge(2,0,2))
    add_edge(graph, Edge(2,1,10))
    add_edge(graph, Edge(2,3,-1))
    # add_edge(graph, Edge(3,1,0))
    add_edge(graph, Edge(3,2,-1))
    return graph

def create_directed_graph(v=4):
    graph = [[] for _ in range(v)]
    add_edge(graph, Edge(0,2))
    add_edge(graph, Edge(1,0))
    add_edge(graph, Edge(2,3))
    # add_edge(graph, Edge(3,0))
    return graph


def create_graph_for_mst(v=4):
    graph = [[] for _ in range(v)]
    
    add_edge(graph, Edge(0, 1, 10))
    add_edge(graph, Edge(0, 2, 15))
    add_edge(graph, Edge(0, 3, 30))
    
    add_edge(graph, Edge(1, 0, 10))
    add_edge(graph, Edge(1, 3, 40))
    
    add_edge(graph, Edge(2, 0, 15))
    add_edge(graph, Edge(2, 3, 50))
    
    add_edge(graph, Edge(3, 1, 40))
    add_edge(graph, Edge(3, 2, 50))
    
    return graph

def mst(graph, src):
    cost = 0
    v = len(graph)
    vis = [False] * v
    pq = []
    heapq.heappush(pq, (0, src))
    
    while pq:
        d, n = heapq.heappop(pq)
        if not vis[n]:
            vis[n] = True
            cost += d
            for edge in graph[n]:
                if not vis[edge.dest]:
                    heapq.heappush(pq, (edge.weight, edge.dest))
    return cost


def created_directed_scc_graph(v=5):
    graph = [[] for _ in range(v)]
    
    add_edge(graph, Edge(0,2))
    add_edge(graph, Edge(0,3))
    
    add_edge(graph, Edge(1,0))
    
    add_edge(graph, Edge(2,1))
    
    add_edge(graph, Edge(3,4))
    
    return graph



def topoSort(graph, i, vis, stack):
    vis[i] = True
    for edge in graph[i]:
        if not vis[edge.dest]:
            topoSort(graph, edge.dest, vis, stack)
    stack.append(i)
    
def kosarajudfs(graph, curr, vis):
    vis[curr] = True
    print(curr, end=" ")
    for edge in graph[curr]:
        if not vis[edge.dest]:
            dfs(graph, edge.dest, vis)

def kosarajuAlgo(graph):
    v = len(graph)
    
    stack = []
    vis = [False] * v
    
    for i in range(v):
        if not vis[i]:
            topoSort(graph, i, vis, stack)
    
    transpose_graph = [[] for _ in range(v)]
    
    for i in range(v):
        vis[i] = False
        for edge in graph[i]:
            transpose_graph[edge.dest].append(Edge(edge.dest, edge.src))
    
    while stack:
        curr = stack.pop()
        if not vis[curr]:
            kosarajudfs(transpose_graph, curr, vis)
            print()
            

def create_graph_for_bridge(v=6):
    v = 5
    graph = [[] for _ in range(v)]
    
    add_edge(graph, Edge(0,1))
    add_edge(graph, Edge(0,2))
    add_edge(graph, Edge(0,3))
    
    add_edge(graph, Edge(1,0))
    add_edge(graph, Edge(1,2))
    
    add_edge(graph, Edge(2,0))
    add_edge(graph, Edge(2,1))
    
    add_edge(graph, Edge(3,0))
    add_edge(graph, Edge(3,4))
    # add_edge(graph, Edge(3,5))
    
    add_edge(graph, Edge(4,3))
    # add_edge(graph, Edge(4,5))
    
    # add_edge(graph, Edge(5,3))
    # add_edge(graph, Edge(5,4))
    
    return graph


def bridge_dfs(graph, curr, vis, dt, low_dt, time, par):
    vis[curr] = True
    time[0] += 1
    dt[curr] = time[0]
    low_dt[curr] = time[0]
    for edge in graph[curr]:
        if edge.dest == par:
            continue
        elif not vis[edge.dest]:
            bridge_dfs(graph, edge.dest, vis, dt, low_dt, time, curr)
            low_dt[curr] = min(low_dt[curr], low_dt[edge.dest])
            if dt[curr] < low_dt[edge.dest]:
                print(f"bridge is: {curr}-----{edge.dest}")
        else:
            low_dt[curr] = min(low_dt[curr], dt[edge.dest])

def getBridge(graph):
    v = len(graph)
    dt = [0] * v
    low_dt = [0] * v
    time = [0]
    vis = [False] * v
    for i in range(v):
        if not vis[i]:
            bridge_dfs(graph, i, vis, dt, low_dt, time, -1)
            
            
def create_graph_arp(v=5):
    graph = [[] for _ in range(v)]
    
    add_edge(graph, Edge(0,1))
    add_edge(graph, Edge(0,2))
    add_edge(graph, Edge(0,3))
    
    add_edge(graph, Edge(1,0))
    add_edge(graph, Edge(1,2))
    
    add_edge(graph, Edge(2,0))
    add_edge(graph, Edge(2,1))
    
    add_edge(graph, Edge(3,0))
    add_edge(graph, Edge(3,4))
    
    add_edge(graph, Edge(4,3))
    
    return graph


def dfs_ap(graph, curr, par, dt, low, vis, time, ap):
    vis[curr] = True
    time[0] += 1
    dt[curr] = low[curr] = time[0]
    children = 0
    for edge in graph[curr]:
        if par == edge.dest:
            continue
        elif vis[edge.dest]:
            low[curr] = min(low[curr], dt[edge.dest])
        else:
            dfs_ap(graph, edge.dest, curr, dt, low, vis, time, ap)
            low[curr] = min(low[curr], low[edge.dest])
            if dt[curr] <= low[edge.dest] and par != -1:
                ap[curr] = True
            children += 1
    
    if par == -1 and children > 1:
        ap[curr] = True

def getAP(graph):
    v = len(graph)
    dt = [0] * v
    low = [0] * v
    time = [0]
    vis = [False] * v
    ap = [False] * v
    
    for i in range(v):
        if not vis[i]:
            dfs_ap(graph, i, -1, dt, low, vis, time, ap)
            
    for i in range(v):
        if ap[i]:
            print("AP:", i)

def isCycleDirected(graph, vis, curr, rec):
    vis[curr] = True
    rec[curr] = True
    
    for edge in graph[curr]:
        if rec[edge.dest]:
            return True
        elif not vis[edge.dest]:
            if isCycleDirected(graph, vis, edge.dest, rec):
                return True
    rec[curr] = False
    return False

def topologicalSortDirected(graph, curr, vis, stack):
    vis[curr] = True
    for edge in graph[curr]:
        if not vis[edge.dest]:
            topologicalSortDirected(graph, edge.dest, vis, stack)
    stack.append(curr)
    
def topSort():
    vis = [False] * 4
    stack = []
    for i in range(4):
        if not vis[i]:
            topologicalSortDirected(directed_graph, i, vis, stack)
    return stack[::-1]


def isCycleUndirected(graph, curr, vis, par):
    vis[curr] = True
    for v in graph[curr]:
        if vis[v.dest] and par != v.dest:
            return True
        elif not vis[v.dest]:
            if isCycleUndirected(graph, v.dest, vis, curr):
                return True
    return False



graph = create_undirected_graph()
print_vertex_neighbours(graph, 2)

print("All vertex with edges:")

print_all_vertex_with_neighbours(graph)

print("Graph BFS Traversal")

bfs(graph)

print("Graph DFS Traversal")
visited = [False] * len(graph)
dfs(graph, 0, visited)
print()

print("All paths")
visited = [False] * len(graph)
start = 0
tar = 1
printAllPath(graph, start, visited, f"{start}", tar )

vis = [False] * len(graph)

print("is cycle undirected graph:", isCycleUndirected(graph, 0, vis, -1))

# print(graph)

directed_graph = create_directed_graph()
vis = [False] * 4
rec = [False] * 4

print('is cycle directed graph:',isCycleDirected(directed_graph, vis, 0, rec))


# topological short


        
print('topological short:', topSort())



# shortest path algo

graph = create_directed_weighted_graph()

disjkstra(graph, 2)

graph = create_directed_wighted_graph_for_bellman()

bellamn_ford(graph, 0)


graph = create_graph_for_mst()

print('mst:', mst(graph, 0))

print('Strongly connected graph')
graph = created_directed_scc_graph()

kosarajuAlgo(graph)

print("find bridge:")

graph = create_graph_for_bridge()

getBridge(graph)

print("find Articulation point:")
graph = create_graph_arp()
getAP(graph)