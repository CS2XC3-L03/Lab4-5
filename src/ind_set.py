from graph import power_set


def is_independent_set(graph, nodes):
    for n1 in nodes:
        for n2 in graph.adj[n1]:
            if n2 in nodes:
                return False
    return True


def maximum_independent_set(graph):
    nodes = [i for i in range(graph.number_of_nodes())]
    powerSet = power_set(nodes)
    max_set = []
    for i in powerSet:
        if is_independent_set(graph, i) and len(i) > len(max_set):
            max_set = i
    return max_set
