from task_3_utils import *

# build the AVL graph
root = None
keys = [10, 20, 30, 25, 28, 27, -1, 17, 24, 5, 6, 55]
for key in keys:
    root = insert(root, key)

# draw the graph
G = nx.Graph()
formatted_edges = format_edges(root.__list__(25))
G.add_edges_from(formatted_edges)
pos = nx.planar_layout(G)
nx.draw(G, pos = pos, with_labels = True)
plt.show()

# Task 1
print("\nTask 1: The highest value on the graph is:", find_max(root), end = "\n" * 2)

# Task 2
print("Task 2: The lowest value on the graph is:", find_min(root), end = "\n" * 2)

# Task 3
print("Task 3: Expected sum:", sum(keys))
print("Task 3: Actual sum:", find_sum(root))