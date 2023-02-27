import graph
import random

# Approx1
def approx1(G):
    C = set()
    G_cp = graph.graph_copy(G)
    while (graph.is_vertex_cover(G, C) == False):
        max_len = -1
        for node in G_cp.adj:
            max_len = max(len(G_cp.adj[node]), max_len)
        for node in G_cp.adj:
            if len(G_cp.adj[node]) == max_len and node not in C:
                v = node
        C.add(v)
        remove_node(G_cp, v)
    return C
    
# Aprrox2
def approx2(G):
    C = set()
    G_cp = graph.graph_copy(G)
    while (graph.is_vertex_cover(G, C) == False):
        v = random.choice(list(G_cp.adj.keys()))
        C.add(v)
    return C

# Aprrox3
def approx3(G):
    C = set()
    G_cp = graph.graph_copy(G)
    while (graph.is_vertex_cover(G, C) == False):
        u = random.choice(list(G_cp.adj.keys()))
        while len(G_cp.adj[u]) == 0:
            u = random.choice(list(G_cp.adj.keys()))
        v = random.choice(G_cp.adj[u])

        C.add(u), C.add(v)
        remove_node(G_cp, u), remove_node(G_cp, v)
    return C

# Helper Function
def remove_node(G, n):
    G.adj.pop(n)
    for node in G.adj.keys():
        if n in G.adj[node]:
            G.adj[node].remove(n)


print("---------------test-----------------------")

gp = graph.create_random_graph(5, 5)
print(approx1(gp))

print(approx2(gp))

print(approx3(gp))
