import matplotlib.pyplot as plt
from graph import create_random_graph, has_cycle

"""
Experiment 1: Determine the probability that a random graph with n nodes abd j edges has a cycle.

We will do this by creating a random graph with 100 nodes and edges from 1 to the maximum number of edges possible. We will then run the has_cycle function 20 times for each edge count and plot the results.
"""


def main():
    NUM_OF_NODES = 100
    NUM_OF_RUNS = 100
    edge_counts = [1, 5, 10, 25, 50, 75, 100, 250, 500, 750, 1000]
    probabilities = []

    for edge_count in edge_counts:
        print(f"Running for edge count {edge_count}")
        count = 0
        for _ in range(NUM_OF_RUNS):
            graph = create_random_graph(NUM_OF_NODES, edge_count)
            if has_cycle(graph):
                count += 1
        probabilities.append(count / NUM_OF_RUNS)
    plt.plot(edge_counts, probabilities)
    plt.plot(edge_counts, probabilities)
    plt.xlabel("Number of edges")
    plt.ylabel("Probability of cycle")
    plt.title("Probability of cycle in random graph")
    plt.show()


if __name__ == "__main__":
    main()
