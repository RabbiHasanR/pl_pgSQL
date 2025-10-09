graphs is network of nodes

node = vertex(vertices)

connection = edge

neighbours


applications of graphs:
1. maps
2. social network
3. delivery network

graphs algorithms:
shortest path
shortest cyclic path
minimum spanning tree(mst)


vertex: every node of graph is a vertex
edge: edge is a connection between two vertex
uni-directional edge:
bi-directional/undirectional edge:

self edge


directed graph
undirected graph

edge based on weight
weighted graph
unweighted graph 

disconected componets graph


storing a graph:
adjacency list:list of lists like [[(0,2)], [(1,2),(1,3)],[(2,0),(2,1),(2,3)],[(3,1),(3,2)]]. for find neighbours from adjacency list time O(x)  x= total neighbours
adjacency matrix:  for find neighbours from adjacency matrix time O(v)  v= total number of vertex
edge list: only edges list like [[0,2],[1,2],[1,3],[2,3]]. list length is number of edges. using edge list can we finst MST
2d matrix(implicit graph):



graph traversals:

breadth first search(BFS), indirecty level order traversal

Depth first search(DFS)

cycling:
directed graph cycle
undirected graph cycle


topological sorting:
work for only directed acyclic graph(DAG)

Directed acyclic graph(DAG) is a directed graph with no cycles. topological sorting is used only for DAGs (not for non DAGs)
It is a linear order of vertices such that every directed edge u -> v, the vertex u comes befor v in the order.



undirected graph cycle detection technique: DFS, BFS, DSU(Disjoint Set Union)

directed path cycle detection technique: DFS,BFS, Topological sorting, graphcolory