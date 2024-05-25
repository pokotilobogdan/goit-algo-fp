import uuid
import heapq

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
    
def get_list_from_tree(root: Node):
    new_list = []
    new_list.append(root.val)
    if root.left is not None:
        new_list.extend(get_list_from_tree(root.left))
    if root.right is not None:
        new_list.extend(get_list_from_tree(root.right))
    return new_list

def get_tree_from_list(root_list: list[int]):
    tree = [Node(root_list[0])]
    for i in range(1, len(root_list)):
        if (i-1) % 2 == 0:
            tree[int((i-1)/2)].left = Node(root_list[i])
            tree.append(tree[int((i-1)/2)].left)
        else:
            tree[int((i-2)/2)].right = Node(root_list[i])
            tree.append(tree[int((i-2)/2)].right)
    return tree[0]

def draw_tree_from_graph(root: Node):
    """
    Takes a binary tree as an argument. Converts it to a heap structure and then draws a result.
    """
    tree_list = get_list_from_tree(root)
    heapq.heapify(tree_list)
    new_root = get_tree_from_list(tree_list)
    draw_tree(new_root)


if __name__ == "__main__":

    # Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    root.right.left.right = Node(20)
    root.right.left.right.right = Node(10)


    # probe_list = get_list_from_tree(root)
    # print(probe_list)
    # heapq.heapify(probe_list)
    # print(probe_list)
    # tree = get_tree_from_list(probe_list)
    # draw_tree(tree)

    # Відображення дерева
    draw_tree(root)
    
    # Перетворюємо бінарне дерево на мінімальну купу, та візуалізуємо його
    draw_tree_from_graph(root)
    plt.show()