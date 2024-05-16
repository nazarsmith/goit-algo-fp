import networkx as nx
import matplotlib.pyplot as plt

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None
    
    def __list__(self, prefix = "root"):
        ret_val = [(str(prefix), str(self.key))]
        if self.left:
            ret_val.append(self.left.__list__(prefix = self.key))
        if self.right:
            ret_val.append(self.right.__list__(prefix = self.key))
        return ret_val
        

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def right_rotate(y):
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x

def insert(root, key):
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

# helper function to format the edges into nx-compatible format
def format_edges(edges, formatted: list = []):
        for l in edges:
            if isinstance(l, list):
                format_edges(l, formatted)
            elif isinstance(l, tuple):
                if len(set(l)) == 2:
                    formatted.append(l)
        return formatted

# Task 1
def find_max(node: AVLNode):
    
    if node:
        highest = node.key
        if node.right:
            highest = find_max(node.right)
        return highest
    else:
        return -1

# Task 2
def find_min(node: AVLNode):
    
    if node:
        lowest = node.key
        if node.left:
            lowest = find_min(node.left)
        return lowest
    else:
        return -1

# Task 3
def find_sum(node: AVLNode, sum: int = 0):
    if node:
        sum += int(node.key)
        if node.left:
            sum = find_sum(node.left, sum)
        if node.right:
            sum = find_sum(node.right, sum)
        # print(sum)
        return sum