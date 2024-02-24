import graph

def is_ind_set(G, L):
    for n1 in L:
        for n2 in G.adj[n1]:
            if n2 in L:
                return False
    return True


def MIS(G):
    nodes = [i for i in range(G.number_of_nodes())]
    powerSet = graph.power_set(nodes)
    max_set = []
    for i in powerSet:
        if is_ind_set(G, i) and len(i) > len(max_set):
            max_set = i
    return max_set
