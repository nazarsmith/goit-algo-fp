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
    root = Node(nodes[0])

    ## helper function to add nodes to a heap and draw it afterward
    def add_item(root, item: Node):

        if root.balance == 0:
            root.left = item
            root.balance += 1

        elif root.balance == 1:
            root.right = item
            root.balance += 1
        
        elif root.left.balance == 0:
            root.left = add_item(root.left, item)
            
        elif root.left.balance == 1:
            root.left.right = item
            root.left.balance += 1
        
        elif root.right.balance == 0:
            root.right = add_item(root.right, item)
        
        elif root.right.balance == 1:
            root.right.right = item
            root.right.balance += 1

        else:
            root.left = add_item(root.left, item)
        return root

    for i in range(len(nodes)):
        if i * 2 + 1 <= len(nodes) - 1:
            root = add_item(root, Node(nodes[i * 2 + 1]))
        if i * 2 + 2 <= len(nodes) - 1:
            root = add_item(root, Node(nodes[i * 2 + 2]))

    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    tree = add_edges(tree, root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()
    return root, tree

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


