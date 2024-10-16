import networkx as nx
import matplotlib.pyplot as plt

# Створення об'єкту графа
G = nx.Graph()

# Додавання вершин
nodes = ["A", "B", "C", "D", "E", "F"]
G.add_nodes_from(nodes)

# Додавання ребер з вагами
edges = [
    ("A", "B", 1),
    ("A", "C", 5),
    ("B", "C", 2),
    ("B", "D", 4),
    ("C", "D", 1),
    ("C", "E", 3),
    ("D", "E", 2),
    ("E", "F", 1),
]
G.add_weighted_edges_from(edges)


def dijkstra_paths(graph, source):
    # Ініціалізація відстаней, попередників та множини невідвіданих вершин
    distances = {vertex: float("infinity") for vertex in graph}
    previous_nodes = {vertex: None for vertex in graph}
    distances[source] = 0
    unvisited = list(graph.nodes)

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float("infinity"):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight.get("weight")

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях та попередника
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    # Відновлення шляхів
    paths = {vertex: [] for vertex in graph}
    for vertex in graph:
        current = vertex
        while current is not None:
            paths[vertex].insert(0, current)
            current = previous_nodes[current]

    return distances, paths


# Знаходження найкоротших шляхів для всіх вершин
shortest_distances = {}
shortest_paths = {}
for node in G.nodes():
    distances, paths = dijkstra_paths(G, node)
    shortest_distances[node] = distances
    shortest_paths[node] = paths

for start_node in shortest_paths:
    print(f"Найкоротші шляхи від {start_node}:")
    for end_node in shortest_paths[start_node]:
        print(
            f"  до {end_node}: Шлях - {shortest_paths[start_node][end_node]}, Відстань - {shortest_distances[start_node][end_node]}"
        )
    print()


# Використання single_source_dijkstra_path з бібліотеки networkx
def nx_dijkstra_paths(graph, source):
    return nx.single_source_dijkstra_path(graph, source)


# Знаходження найкоротших шляхів для всіх вершин
shortest_paths = {node: nx_dijkstra_paths(G, node) for node in G.nodes()}

for start_node in shortest_paths:
    print(f"Найкоротші шляхи від  {start_node}:")
    for end_node in shortest_paths[start_node]:
        print(f" до {end_node}: {shortest_paths[start_node][end_node]}")
    print()

# Візуалізація графу
pos = nx.spring_layout(G)  # позиції для всіх вершин
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="skyblue",
    node_size=2000,
    font_size=15,
    font_color="black",
    edge_color="gray",
)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
