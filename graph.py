import random
from collections import deque

# Undirected graph using an adjacency list
class Graph:
    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes():
        return len()


# Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1: True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False


# Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False


# Use the methods below to determine minimum vertex covers


def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy


def power_set(set):
    if set == []:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])


def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not (start in C or end in C):
                return False
    return True


def MVC(G):
    nodes = [i for i in range(G.get_size())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover


def BFS2(G, node1, node2):
    Q, visited = deque([(node1, [node1])]), set()
    while Q:
        (vertex, path) = Q.popleft()
        if vertex in visited:
            continue
        if vertex == node2:
            return path
        visited.add(vertex)
        for neighbour in G.adj[vertex]:
            Q.append((neighbour, [*path, neighbour]))
    return []


def DFS2(G, node1, node2):
    S, visited = [(node1, [node1])], set()
    while S:
        (vertex, path) = S.pop()
        if vertex in visited:
            continue
        if vertex == node2:
            return path
        visited.add(vertex)
        for neighbour in G.adj[vertex]:
            S.append((neighbour, [*path, neighbour]))
    return []


# def BFS3(graph, node1):
#     visited, Q, pred = {node1}, deque([node1]), {node1: None}
#     while Q:
#         current_node = Q.popleft()
#         for neighbour in graph.adj[current_node]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 Q.append(neighbour)
#                 pred[neighbour] = current_node
#     return pred


# def DFS3(graph, node1):
#     visited, S, pred = {node1}, [node1], {node1: None}
#     while S:
#         current_node = S.pop()
#         for neighbour in graph.adj[current_node]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 S.append(neighbour)
#                 pred[neighbour] = current_node
#     return pred


def has_cycle(G):
    visited = set()
    for node in G.adj:
        if node not in visited and has_cycle_helper(G, node, visited, None):
            return True
    return False


def has_cycle_helper(G, node, visited, parent):
    visited.add(node)
    for neighbour in G.adj[node]:
        if neighbour not in visited:
            has_cycle_helper(G, neighbour, visited, node)
        elif parent and (neighbour != parent):
            return True
    return False


def is_connected(G):
    # If the graph is empty, it is connected
    if not G.adj:
        return True
    first_node = list(G.adj.keys())[0]
    S, visited = [first_node], {first_node}
    while S:
        current_node = S.pop()
        for neighbour in G.adj[current_node]:
            if neighbour not in visited:
                visited.add(neighbour)
                S.append(neighbour)
    return len(visited) == len(G.adj)


def create_random_graph(i, j):
    graph = Graph(i)
    created_edges = set()
    if j > i * (i - 1) / 2:
        j = i * (i - 1) / 2
    for _ in range(j):
        node1 = random.randint(0, i - 1)
        node2 = random.randint(0, i - 1)
        while any([
            (node1, node2) in created_edges,
            (node2, node1) in created_edges,
            node1 == node2,
        ]):
            node1 = random.randint(0, i - 1)
            node2 = random.randint(0, i - 1)
        created_edges.add((node1, node2))
        created_edges.add((node2, node1))
        graph.add_edge(node1, node2)
    return graph


graph = create_random_graph(5, 5)

print(graph.adj)

graph2 = Graph(3)
graph2.add_edge(0, 1)

print(is_connected(graph2)) # False 0, 1 but not 2
graph2.add_edge(1, 2)
print(is_connected(graph2)) # True 0, 1, 2
