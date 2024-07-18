import random
from collections import deque


class Graph:
    """
    Undirected graph using adjacency list representation
    """

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

    def number_of_nodes(self):
        return len(self.adj)


def bfs(graph, node1, node2):
    queue = deque([node1])
    marked = {node1: True}
    for node in graph.adj:
        if node != node1:
            marked[node] = False
    while len(queue) != 0:
        current_node = queue.popleft()
        for node in graph.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                queue.append(node)
                marked[node] = True
    return False


def dfs(graph, node1, node2):
    stack = [node1]
    marked = {}
    for node in graph.adj:
        marked[node] = False
    while len(stack) != 0:
        current_node = stack.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in graph.adj[current_node]:
                if node == node2:
                    return True
                stack.append(node)
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


def is_vertex_cover(graph, cover_set):
    for start in graph.adj:
        for end in graph.adj[start]:
            if not (start in cover_set or end in cover_set):
                return False
    return True


def minimum_vertex_cover(graph):
    nodes = [i for i in range(graph.number_of_nodes())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(graph, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover


def bfs2(graph, node1, node2):
    queue, visited = deque([(node1, [node1])]), set()
    while queue:
        (vertex, path) = queue.popleft()
        if vertex in visited:
            continue
        if vertex == node2:
            return path
        visited.add(vertex)
        for neighbour in graph.adj[vertex]:
            queue.append((neighbour, [*path, neighbour]))
    return []


def dfs2(graph, node1, node2):
    stack, visited = [(node1, [node1])], set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex in visited:
            continue
        if vertex == node2:
            return path
        visited.add(vertex)
        for neighbour in graph.adj[vertex]:
            stack.append((neighbour, [*path, neighbour]))
    return []


def bfs3(graph, node1):
    visited, queue, pred = {node1}, deque([node1]), {}
    while queue:
        current_node = queue.popleft()
        for neighbour in graph.adj[current_node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                pred[neighbour] = current_node
    return pred


def dfs3(graph, node1):
    visited, stack, pred = {node1}, [node1], {}
    while stack:
        current_node = stack.pop()
        for neighbour in graph.adj[current_node]:
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)
                pred[neighbour] = current_node
    return pred


def has_cycle(graph):
    visited = set()
    for node in graph.adj:
        if node not in visited and has_cycle_helper(graph, node, visited):
            return True
    return False


def has_cycle_helper(graph, node, visited, parent=None):
    visited.add(node)
    for neighbour in graph.adj[node]:
        if neighbour not in visited:
            has_cycle_helper(graph, neighbour, visited, node)
        elif neighbour != parent:
            return True
    return False


def is_connected(graph):
    # If the graph is empty, it is connected
    if not graph.adj:
        return True
    first_node = list(graph.adj.keys())[0]
    stack, visited = [first_node], {first_node}
    while stack:
        current_node = stack.pop()
        for neighbour in graph.adj[current_node]:
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)
    return len(visited) == len(graph.adj)


def create_random_graph(i, j):
    graph = Graph(i)
    created_edges = set()
    if j > i * (i - 1) / 2:
        j = i * (i - 1) / 2
    for _ in range(j):
        node1 = random.randint(0, i - 1)
        node2 = random.randint(0, i - 1)
        while any(
            [
                (node1, node2) in created_edges,
                (node2, node1) in created_edges,
                node1 == node2,
            ]
        ):
            node1 = random.randint(0, i - 1)
            node2 = random.randint(0, i - 1)
        created_edges.add((node1, node2))
        created_edges.add((node2, node1))
        graph.add_edge(node1, node2)
    return graph


def copy_graph(graph):
    graph_copy = Graph(graph.number_of_nodes())
    for n1 in graph.adj.keys():
        for n2 in graph.adjacent_nodes(n1):
            graph_copy.add_edge(n1, n2)
    return graph_copy
