import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = [node for node in distances.keys()]

    while unvisited:
        
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        # САМЕ ТУТ я використав купу, щоб знайти вузол з найменшою відстаню до нього від початкового
        distance_to_vertex, current_vertex = heapq.heappop([(distances[node], node) for node in unvisited])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу (ми не можемо більше дібратись до жодного з вузлів)
        if distance_to_vertex == float('infinity'):
            break

        for neighbor, stats in graph[current_vertex].items():
            distance = distances[current_vertex] + stats['weight']

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances


if __name__ == "__main__":

    graph_dict = {
        'A': {'B': {'weight': 5}, 'C': {'weight': 10}},
        'B': {'A': {'weight': 5}, 'D': {'weight': 3}},
        'C': {'A': {'weight': 10}, 'D': {'weight': 2}, 'E': {'weight': 1}},
        'D': {'B': {'weight': 3}, 'C': {'weight': 2}, 'E': {'weight': 4}},
        'E': {'D': {'weight': 4}, 'C': {'weight': 1}}
    }

    # Створення графа зі словника
    G = nx.from_dict_of_dicts(graph_dict)

    # Візуалізація графа
    pos = nx.spring_layout(G, seed=50)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Виклик функції для вершини A
    print(dijkstra(graph_dict, 'A'))

    plt.show()
