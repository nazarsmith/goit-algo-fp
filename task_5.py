from task_4 import *
from collections import deque
from matplotlib import colors as clr
from copy import deepcopy

def get_specs(graph):
    colors = [specs['color'] for _, specs in graph.items()]
    labels = {node: specs['label'] for node, specs in graph.items()}
    return colors, labels

def dfs_recursive(graph, vertex, visited = None, color = [0.5, 0.5, 0.5]):
    if visited is None:
        visited = []
    visited.append(vertex)
    color[0] -= 0.025
    color[1] += 0.025
    color[2] -= 0.025
    graph[vertex]["color"] = clr.to_hex(color)
    for neighbor in graph[vertex]["connected_edges"]:
        try:
            if neighbor not in visited:
                dfs_recursive(graph, neighbor, visited, color)
        except:
            pass
    colors, labels = get_specs(graph)

    return visited, colors, labels

def bfs_recursive(graph, queue, visited = None, color = [0.5, 0.5, 0.5]):
    # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
    if not visited:
        visited = []
    # Якщо черга порожня, завершуємо рекурсію
    if not queue:
        return
    # Вилучаємо вершину з початку черги
    vertex = queue.popleft()
    # Перевіряємо, чи відвідували раніше дану вершину
    if vertex not in visited:
        # Додаємо вершину до множини відвіданих вершин.
        visited.append(vertex)
        # Додаємо невідвіданих сусідів даної вершини в кінець черги.
        color[0] -= 0.025
        color[1] += 0.025
        color[2] -= 0.025
        graph[vertex]["color"] = clr.to_hex(color)
        queue.extend(set(graph[vertex]["connected_edges"]) - set(visited))
    # Рекурсивний виклик функції з тією ж чергою та множиною відвіданих вершин
    bfs_recursive(graph, queue, visited, color = color)
    
    colors, labels = get_specs(graph)

    return visited, colors, labels


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

    # draw original binary trees
    labels, tree = draw_tree(root)

    # get the nodes of the tree and analyze
    nodes = tree.nodes(data = True)
    node_edge_dict = {}
    for node in nodes:
        # get the edges that connect nodes
        edges = list(tree.edges(node[0]))
        # create template for future DFS/BFS graph specs
        graph = {
            "connected_edges": [],
            "label": None,
            "color": "#350917"
        }
        # update the specs
        if not edges:
            node_edge_dict[node[0]] = graph
            node_edge_dict[node[0]]["label"] = labels[node[0]]
            continue
        while edges:
            edge = edges.pop(0)[1]
            graph["connected_edges"].append(edge)
            graph["label"] = labels[node[0]]
            node_edge_dict[node[0]] = graph
    
    # make a copy of the nodes/edges to illustrate BFS
    node_edge_dict_bfs = deepcopy(node_edge_dict)

    # do the DFS search
    visited, colors, labels = dfs_recursive(node_edge_dict, list(node_edge_dict.keys())[0])
    visited = [labels[node] for node in visited]
    print("Visited order (DFS):", visited)
    # draw the tree after DFS was applied
    draw_tree(root, colors = colors, labels = labels, title = "DFS")

    # do the BFS search
    visited_bfs, colors, labels = bfs_recursive(node_edge_dict_bfs, deque([list(node_edge_dict_bfs.keys())[0]]))
    visited_bfs = [labels[node] for node in visited_bfs]
    print("Visited order (BFS):", visited_bfs)
    # draw the tree after BFS was applied   
    draw_tree(root, colors = colors, labels = labels, title = "BFS (right to left)")