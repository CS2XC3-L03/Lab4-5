import matplotlib.pyplot as plot
import graph
import approxfunc

def ept3_test(node_num, graphs_num):
    mvc_list, approx1_list, approx2_list, approx3_list = [], [], [], []
    max_edge_num = node_num * (node_num - 1) // 2 # n*(n-1)/2 formula to calc max edges give num of nodes
    for edge_num in range(max_edge_num + 1):
        mvc_sum, approx1_sum, approx2_sum, approx3_sum = 0, 0, 0, 0
        for _ in range(graphs_num):
            gp = graph.create_random_graph(node_num, edge_num)
            mvc_sum     += len(graph.MVC(gp))
            approx1_sum += len(approxfunc.approx1(gp))
            approx2_sum += len(approxfunc.approx2(gp))
            approx3_sum += len(approxfunc.approx3(gp))
        
        mvc_list.append(mvc_sum / graphs_num)
        approx1_list.append(approx1_sum / graphs_num)
        approx2_list.append(approx2_sum / graphs_num)
        approx3_list.append(approx3_sum / graphs_num)

    print("plotting...")

    plot.plot(mvc_list, label="MVC")
    plot.plot(approx1_list, label="Approximation 1")
    plot.plot(approx2_list, label="Approximation 2")
    plot.plot(approx3_list, label="Approximation 3")
    plot.legend()
    plot.xlabel("Number of Edges")
    plot.ylabel("Size of Vertex Cover Approximations")
    plot.title(f"Accuracy Comparisons of 3 Different Algorithms of Vertex Cover Approximations On {node_num} Node Nums")
    plot.show()

print("-------------------------------exp3----------------------------------")
ept3_test(5, 1000)

ept3_test(7, 1000)

ept3_test(9, 1000)
