from graph import create_random_graph, minimum_vertex_cover
from ind_set import maximum_independent_set


def experiment4(node_num):
    max_edge_num = (
        node_num * (node_num - 1) // 2
    )  # n*(n-1)/2 formula to calc max edges give num of nodes
    for number_of_edges in range(max_edge_num + 1):
        graph = create_random_graph(node_num, number_of_edges)
        cover_set = minimum_vertex_cover(graph)
        independentSet = maximum_independent_set(graph)

        print(f"The size of MVC: {len(cover_set)}")
        print(f"The size of MIS: {len(independentSet)}")
        total = len(cover_set) + len(independentSet)
        if total == node_num:
            print(
                f"The node_num is {node_num}, sum of the size of MVC and MIS is {total}, which are equal."
            )
        else:
            print("something wrong with the code")


def main():
    experiment4(5)
    experiment4(7)
    experiment4(9)


if __name__ == "__main__":
    main()
