from collections import deque
import uuid

import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла
        
    def __repr__(self):
        return str(self.val)

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
    plt.show(block=False)

def bfs_tree(root, order_storage=[]):
    
    queue = deque()
    queue.append(root)
    
    while queue:
        visited = queue.popleft()
        order_storage.append(visited)
        if visited.left: queue.append(visited.left)
        if visited.right: queue.append(visited.right)
        
    for i, node in enumerate(order_storage):
        order_color = round(255/len(order_storage)*i)
        node.color = f"#{order_color:02x}{order_color:02x}{order_color:02x}"
    return order_storage

def dfs_tree(root, order_storage=[]):
    order_storage.append(root)
    if root.left: dfs_tree(root.left, order_storage)
    if root.right: dfs_tree(root.right, order_storage)
    for i, node in enumerate(order_storage):
        order_color = round(255/len(order_storage)*i)
        node.color = f"#{order_color:02x}{order_color:02x}{order_color:02x}"
    return order_storage
    
            

if __name__ == "__main__":

    # Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.left.right.right = Node(100)
    root.right = Node(1)
    root.right.left = Node(3)
    root.right.left.left = Node(11)
    root.right.left.right = Node(6)
    

    # print(bfs_iterative())

    print("BFS: ", bfs_tree(root))
    draw_tree(root)
    
    print("DFS: ", dfs_tree(root))
    draw_tree(root)
    
    plt.show()