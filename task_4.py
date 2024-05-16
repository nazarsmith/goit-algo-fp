import uuid

import networkx as nx
import matplotlib.pyplot as plt

import heapq

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.balance = 0
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    # plt.show()
    return tree

def draw_heap(nx_tree, root):
    nodes = [node[-1]["label"] for node in nx_tree.nodes(data = True)]
    heapq.heapify(nodes)

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
    return root, tree

if __name__ == "__main__":
    # Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    root.right.left.right = Node(13)
    root.left.left.right = Node(173)
    root.left.right.right = Node(2)
    root.left.right.left = Node(1)

    # Відображення дерева
    tree = draw_tree(root)

    # Відображення купи
    heap, heap_graph = draw_heap(tree, root)


