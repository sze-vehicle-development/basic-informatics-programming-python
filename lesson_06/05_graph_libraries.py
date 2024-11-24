import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()  # For undirected graph
G.add_node(1)  # Add node
G.add_nodes_from([2, 3, 4])  # Add nodes
G.add_edge(1, 2)  # Add edge
G.add_edges_from([(1, 3), (1, 4)])  # Add edges

nx.draw(G, with_labels=True)
plt.show()
