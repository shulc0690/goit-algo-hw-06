import networkx as nx
import matplotlib.pyplot as plt

# Створюємо обьєкт графа
G = nx.Graph()

# Додаємо вершини
nodes = ["A", "B", "C", "D", "E", "F"]
G.add_nodes_from(nodes)

# Додаємо ребра
edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("C", "D"),
    ("C", "E"),
    ("D", "E"),
    ("E", "F"),
]
G.add_edges_from(edges)


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    print(stack)
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


start = "A"
goal = "F"

dfs_result = list(dfs_paths(G, start, goal))
bfs_result = list(bfs_paths(G, start, goal))

print(f"DFS шлях з {start} до {goal}:")
for path in dfs_result:
    print(path)

print(f"\nBFS шлях з {start} до {goal}:")
for path in bfs_result:
    print(path)
