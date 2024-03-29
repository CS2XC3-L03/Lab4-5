import matplotlib.pyplot as plt
from graph import create_random_graph, is_connected


def main():
    """
    Experiment 2: Determine the probability that a random graph with n nodes and j edges is connected.
    """
    NUM_OF_NODES = 100
    NUM_OF_RUNS = 100
    edge_counts = [1, 5, 10, 25, 50, 75, 100, 250, 500, 750, 1000]
    probabilities = []

    for edge_count in edge_counts:
        print(f"Running for edge count {edge_count}")
        count = 0
        for _ in range(NUM_OF_RUNS):
            graph = create_random_graph(NUM_OF_NODES, edge_count)
            if is_connected(graph):
                count += 1
        probabilities.append(count / NUM_OF_RUNS)
    plt.plot(edge_counts, probabilities)
    plt.xlabel("Number of edges (j)")
    plt.ylabel("Probability of connectedness")
    plt.title("Probability of connectedness in random graph with 100 nodes and j edges")
    plt.show()


if __name__ == "__main__":
    main()
