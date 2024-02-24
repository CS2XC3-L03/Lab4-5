import graph
import ind_set


def experiment4(node_num):
    print("----------------------------experiment 4------------------------------")
    max_edge_num = node_num * (node_num - 1) // 2 # n*(n-1)/2 formula to calc max edges give num of nodes
    for num_of_edges in range(max_edge_num + 1):
        gp = graph.create_random_graph(node_num, num_of_edges)
        C = graph.MVC(gp)
        S = ind_set.MIS(gp)

        print(f"The size of MVC: {len(C)}")
        print(f"The size of MIS: {len(S)}")
        summ = len(C) + len(S)
        if ((summ == node_num)):
            print(f"The node_num is {node_num}, sum of the size of MVC and MIS is {summ}, which are equal.")
        else:
            print("something wrong with the code")
        print("----------------------------experiment 4------------------------------")   


def main():
    experiment4(5)
    experiment4(7)
    experiment4(9)


if __name__ == "__main__":
    main()