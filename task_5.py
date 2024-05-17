from task_4 import *
from collections import deque
from matplotlib import colors
from copy import deepcopy

def dfs_recursive(graph, vertex, visited=None, color = [0.25, 0.1, 0.15]):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(graph[vertex]["label"], end=' ')  # Відвідуємо вершину
    updated_colors = [c + 0.017 for c in color]
    graph[vertex]["color"] = colors.to_hex(updated_colors)
    for neighbor in graph[vertex]["connected_edges"]:
        try:
            if neighbor not in visited:
                dfs_recursive(graph, neighbor, visited, updated_colors)
        except:
            pass


def bfs_recursive(graph, queue, visited=None):
    # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
    if not visited:
        visited = set()
    # Якщо черга порожня, завершуємо рекурсію
    if not queue:
        return
    # Вилучаємо вершину з початку черги
    vertex = queue.popleft()
    # Перевіряємо, чи відвідували раніше дану вершину
    if vertex not in visited:
        # Якщо не відвідували, друкуємо вершину
        print(vertex, end=" ")
        # Додаємо вершину до множини відвіданих вершин.
        visited.add(vertex)
        # Додаємо невідвіданих сусідів даної вершини в кінець черги.
        try:
            queue.extend(set(graph[vertex]) - visited)
        except:
            pass
    # Рекурсивний виклик функції з тією ж чергою та множиною відвіданих вершин
    bfs_recursive(graph, queue, visited)



if __name__ == "__main__":

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
    labels, tree = draw_tree(root)
    # print(labels)

    nodes = tree.nodes(data = True)
    node_edge_dict = {}
    for node in nodes:
        edges = list(tree.edges(node[0]))
        graph = {
            "connected_edges": [],
            "label": None,
            "color": "#350917"
        }
        if not edges:
            node_edge_dict[node[0]] = graph
            node_edge_dict[node[0]]["label"] = labels[node[0]]
            continue
        while edges:
            edge = edges.pop(0)[1]
            graph["connected_edges"].append(edge)
            graph["label"] = labels[node[0]]
            node_edge_dict[node[0]] = graph
    
    node_edge_dict_bfs = deepcopy(node_edge_dict)
        # connected_edges = []

    for k, v in node_edge_dict.items():
        print(k, v)

    dfs_recursive(node_edge_dict, list(node_edge_dict.keys())[0])
    # bfs_recursive(node_edge_dict, deque([0]))

    for k, v in node_edge_dict.items():
        print(k, v)
    
    print("BFS original")
    for k, v in node_edge_dict_bfs.items():
        print(k, v)