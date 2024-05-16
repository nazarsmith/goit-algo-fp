import uuid

import networkx as nx
import matplotlib.pyplot as plt

import heapq

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
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
    plt.show()
    return tree

def draw_heap(nx_tree, root):
    nodes = [node[-1]["label"] for node in nx_tree.nodes(data = True)]
    print(nx_tree.nodes(data = True))
    heapq.heapify(nodes)
    print(nodes)

    root = Node(nodes[0])
    print(root, root.val, root.left, root.right)

    def add_item_left(root, item: Node):
        
        value = item.val
        print("left", root.val, root.left, root.right, value)

        if not root.left:
            root.left = item
            # root.left = add_item(root.left, item)
        elif root.left:
            root.left = add_item_left(root.left, item)
        # elif value >= root.left.val and value >= root.val:
        #     print(value, "bigger than", root.left.val)
        #     root.left = add_item_left(root.left, item)
        # elif root.left.left and root.right.right:
        #     root.right.left = item
            # else:
            #     root.left.left = item
        return root
    
    def add_item_right(root, item: Node):
        
        value = item.val
        print("right", root.val, root.left, root.right, value)

        if not root.right:
            root.right = item
        elif root.right:
            root.right = add_item_right(root.right, item)
        # elif value > root.left.val and root.right:
        #     root.left = add_item_right(root.left, item)
        else:
            root.right = add_item_right(root.right, item)
        return root

    for i in range(len(nodes)):
        # print(i, nodes[i * 2 + 1])
        # print(i, nodes[i * 2 + 2])
        print(i)
        if i * 2 + 1 <= len(nodes) - 1:
            root = add_item_left(root, Node(nodes[i * 2 + 1]))
        if i * 2 + 2 <= len(nodes) - 1:
            root = add_item_right(root, Node(nodes[i * 2 + 2]))
        # if nodes[i * 2 + 1] <= len(nodes) - 1:
        #     root.left = None
        # if nodes[i * 2 + 2] <= len(nodes) - 1:
        #     root.right = None
            # try:
                # root.left = Node(nodes[i * 2 + 1])
                # root.right = Node(nodes[i * 2 + 2])
            # root = add_item(root, Node(nodes[i * 2 + 1]))
            # root = add_item(root, Node(nodes[i * 2 + 2]))
            # except:
            #     continue

    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    tree = add_edges(tree, root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева
tree = draw_tree(root)

draw_heap(tree, root)


# for node in nodes:
# print(heap)
