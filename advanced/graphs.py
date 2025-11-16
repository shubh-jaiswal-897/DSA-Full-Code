"""
Graph Data Structures and Algorithms in Python

This module provides implementations of:
1. Graph representations (Adjacency List, Adjacency Matrix)
2. Depth-First Search (DFS)
3. Breadth-First Search (BFS)
4. Shortest Path Algorithms (Dijkstra, Bellman-Ford)

Time Complexities:
- DFS/BFS: O(V + E)
- Dijkstra: O((V + E) log V) with heap
- Bellman-Ford: O(V * E)
"""

from collections import defaultdict, deque
import heapq

class Graph:
    def __init__(self, directed=False):
        self.adj_list = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v, weight=1):
        """Add an edge from u to v with optional weight."""
        self.adj_list[u].append((v, weight))
        if not self.directed:
            self.adj_list[v].append((u, weight))

    def get_vertices(self):
        """Return all vertices in the graph."""
        return list(self.adj_list.keys())

    def get_edges(self):
        """Return all edges in the graph."""
        edges = []
        for u in self.adj_list:
            for v, w in self.adj_list[u]:
                edges.append((u, v, w))
        return edges

    def __str__(self):
        return str(dict(self.adj_list))

class AdjacencyMatrix:
    def __init__(self, vertices, directed=False):
        self.vertices = vertices
        self.directed = directed
        self.matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, weight=1):
        """Add an edge from u to v with weight."""
        self.matrix[u][v] = weight
        if not self.directed:
            self.matrix[v][u] = weight

    def get_edges(self):
        """Return all edges."""
        edges = []
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.matrix[i][j] != 0:
                    edges.append((i, j, self.matrix[i][j]))
        return edges

    def __str__(self):
        return "\n".join([str(row) for row in self.matrix])

# Graph Traversal Algorithms
def dfs(graph, start, visited=None):
    """Depth-First Search traversal."""
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]
    for neighbor, _ in graph.adj_list[start]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    return result

def bfs(graph, start):
    """Breadth-First Search traversal."""
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbor, _ in graph.adj_list[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result

# Shortest Path Algorithms
def dijkstra(graph, start):
    """Dijkstra's algorithm for shortest path from start to all vertices."""
    distances = {vertex: float('inf') for vertex in graph.get_vertices()}
    distances[start] = 0
    priority_queue = [(0, start)]  # (distance, vertex)
    previous = {vertex: None for vertex in graph.get_vertices()}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.adj_list[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous

def bellman_ford(graph, start):
    """Bellman-Ford algorithm for shortest path, handles negative weights."""
    distances = {vertex: float('inf') for vertex in graph.get_vertices()}
    distances[start] = 0
    previous = {vertex: None for vertex in graph.get_vertices()}

    vertices = graph.get_vertices()
    edges = graph.get_edges()

    # Relax edges |V| - 1 times
    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                previous[v] = u

    # Check for negative cycles
    for u, v, w in edges:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            raise ValueError("Graph contains negative cycle")

    return distances, previous

def reconstruct_path(previous, start, end):
    """Reconstruct the path from start to end using previous dictionary."""
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    if path[0] == start:
        return path
    return []

# Example usage and test cases
if __name__ == "__main__":
    # Create a graph
    g = Graph()
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 1)
    g.add_edge(1, 3, 1)
    g.add_edge(2, 1, 2)
    g.add_edge(2, 3, 5)
    g.add_edge(3, 4, 3)

    print("Graph:", g)
    print("DFS from 0:", dfs(g, 0))
    print("BFS from 0:", bfs(g, 0))

    # Shortest paths
    distances, previous = dijkstra(g, 0)
    print("Dijkstra distances from 0:", distances)
    print("Path 0 to 3:", reconstruct_path(previous, 0, 3))

    # Bellman-Ford (add negative weight edge for demo)
    g2 = Graph()
    g2.add_edge(0, 1, 4)
    g2.add_edge(0, 2, 1)
    g2.add_edge(1, 2, -2)  # Negative weight
    g2.add_edge(2, 3, 3)
    try:
        distances2, previous2 = bellman_ford(g2, 0)
        print("Bellman-Ford distances from 0:", distances2)
    except ValueError as e:
        print("Bellman-Ford error:", e)

    # Adjacency Matrix
    am = AdjacencyMatrix(5)
    am.add_edge(0, 1, 1)
    am.add_edge(0, 2, 1)
    am.add_edge(1, 3, 1)
    print("Adjacency Matrix:")
    print(am)
