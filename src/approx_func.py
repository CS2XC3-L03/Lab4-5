from graph import copy_graph, is_vertex_cover
import random


def approx1(graph):
    cover_set = set()
    graph_copy = copy_graph(graph)
    while is_vertex_cover(graph, cover_set) == False:
        max_len = -1
        for node in graph_copy.adj:
            max_len = max(len(graph_copy.adj[node]), max_len)
        for node in graph_copy.adj:
            if len(graph_copy.adj[node]) == max_len and node not in cover_set:
                v = node
        cover_set.add(v)
        remove_node(graph_copy, v)
    return cover_set


def approx2(graph):
    cover_set = set()
    graph_copy = copy_graph(graph)
    while is_vertex_cover(graph, cover_set) == False:
        v = random.choice(list(graph_copy.adj.keys()))
        cover_set.add(v)
    return cover_set


def approx3(graph):
    cover_set = set()
    graph_copy = copy_graph(graph)
    while is_vertex_cover(graph, cover_set) == False:
        u = random.choice(list(graph_copy.adj.keys()))
        while len(graph_copy.adj[u]) == 0:
            u = random.choice(list(graph_copy.adj.keys()))
        v = random.choice(graph_copy.adj[u])

        cover_set.add(u)
        cover_set.add(v)
        remove_node(graph_copy, u)
        remove_node(graph_copy, v)
    return cover_set


def remove_node(graph, target_node):
    graph.adj.pop(target_node)
    for node in graph.adj.keys():
        if target_node in graph.adj[node]:
            graph.adj[node].remove(target_node)
