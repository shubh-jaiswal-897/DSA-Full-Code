"""
Clone Graph Problem Implementation in Python

Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.

Time Complexity: O(V + E)
"""

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node):
    """
    Clone the graph using DFS.
    """
    if not node:
        return None

    visited = {}

    def dfs(current):
        if current in visited:
            return visited[current]

        # Create clone
        clone = Node(current.val)
        visited[current] = clone

        # Clone neighbors
        for neighbor in current.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    return dfs(node)

# Example usage and test cases
if __name__ == "__main__":
    # Create a simple graph: 1 -- 2
    node1 = Node(1)
    node2 = Node(2)
    node1.neighbors = [node2]
    node2.neighbors = [node1]

    cloned = clone_graph(node1)
    print("Original node 1 val:", node1.val)
    print("Cloned node 1 val:", cloned.val)
    print("Original node 1 neighbors:", [n.val for n in node1.neighbors])
    print("Cloned node 1 neighbors:", [n.val for n in cloned.neighbors])

    # Check if they are different objects
    print("Are original and cloned the same object?", node1 is cloned)
    print("Are neighbors the same object?", node1.neighbors[0] is cloned.neighbors[0])
