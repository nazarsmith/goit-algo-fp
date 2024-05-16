from task_3_utils import GraphWorkshop
from task_4 import Node, add_edges

import matplotlib.pyplot as plt
import heapq
import networkx as nx

nodes = {
        1: [11, 20, 27, 2],
        2: [1, 3, 21],
        3: [2, 15],
        4: [24, 25],
        5: [6],
        6: [5, 30, 7],
        7: [6, 8, 25, 9],
        8: [7, 30, 27],
        9: [7, 11, 10],
        10: [9],
        11: [9, 1, 12],
        12: [11, 13, 14],
        13: [12, 16, 18],
        14: [13, 12, 15, 17],
        15: [22, 3, 14],
        16: [13, 23],
        17: [29, 18, 14],
        18: [13, 17],
        19: [31, 20],
        20: [19, 1],
        21: [2],
        22:[15],
        23: [25, 16],
        24: [4, 6],
        25: [4, 24, 23],
        26: [30, 27],
        27: [26, 1, 8, 28, 19],
        28: [27],
        29: [],
        30: [6, 26]
    }

graph_workshop = GraphWorkshop(nodes)

## Task 1
graph_workshop.construct_undirected_graph()
un_graph = graph_workshop.un_G
graph_workshop.draw_graph(un_graph)
un_graph_props = graph_workshop.get_graph_properties(un_graph)
nodes, graph = graph_workshop.aggregate_properties(un_graph, un_graph_props)

def draw_heap(nodes):
    # build min heap
    h = []
    for value in nodes:
        heapq.heappush(h, value)
    nodes = [heapq.heappop(h) for _ in range(len(h))]

    # create a binary min heap and draw it
    new_tree = []
    for i in range(len(nodes)):
        new_tree.append(Node(nodes[i]))

    for i in range(len(new_tree)):
        if i * 2 + 1 <= len(new_tree) - 1:
            new_tree[i].left = new_tree[i * 2 + 1]
        if i * 2 + 2 <= len(new_tree) - 1:
            new_tree[i].right = new_tree[i * 2 + 2]

    tree = nx.DiGraph()
    pos = {new_tree[0].id: (0, 0)}
    tree = add_edges(tree, new_tree[0], pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()
    return labels, new_tree, tree

## Task 3
print("\nTask 3:\n")
nodes = list(un_graph.nodes())
heapq.heapify(nodes)

labels, _, tree = draw_heap(nodes)
leafs = []
for node in tree.degree():
    if node[-1] <= 1:
        leafs.append(labels[node[0]])

print("Leaves", leafs)

for i in range(len(leafs) - 1):
    print(
        f"Shortest path from {leafs[i]} to {leafs[i + 1]}:",
        graph_workshop.dij(
            graph = un_graph, source = leafs[i], target = leafs[i + 1]
        )
    )