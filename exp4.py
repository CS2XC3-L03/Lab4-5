import graph
import ind_set


# --------------------- Experiment 4 -------------------------
def ept4_test(node_num):
    print("----------------------------ept4-test------------------------------")
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
        print("----------------------------ept4-test------------------------------")   



# --------------------- Experiment 4 Test Cases -------------------------

ept4_test(5)

ept4_test(7)

ept4_test(9)
