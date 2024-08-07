import matplotlib.pyplot as plt
from graph import create_random_graph, has_cycle


def main():
    """
    Experiment 1: Determine the probability that a random graph with n nodes and j edges has a cycle.
    """

    number_of_nodes = 100
    number_of_runs = 100
    edge_counts = [1, 5, 10, 25, 50, 75, 100, 250, 500, 750, 1000]
    probabilities = []

    for edge_count in edge_counts:
        print(f"Running for edge count {edge_count}")
        count = 0
        for _ in range(number_of_runs):
            graph = create_random_graph(number_of_nodes, edge_count)
            if has_cycle(graph):
                count += 1
        probabilities.append(count / number_of_runs)

    plt.plot(edge_counts, probabilities)
    plt.plot(edge_counts, probabilities)

    plt.xlabel("Number of edges (j)")
    plt.ylabel("Probability of cycle")
    plt.title("Probability of cycle in random graph with 100 nodes and j edges")

    plt.show()


if __name__ == "__main__":
    main()
