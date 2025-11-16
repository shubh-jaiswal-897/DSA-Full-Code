"""
Disjoint Set (Union-Find) Implementation in Python

Disjoint Set is a data structure that keeps track of a set of elements partitioned into disjoint subsets.
It supports two main operations:
- Find: Determine which subset a particular element is in
- Union: Join two subsets into a single subset

Time Complexities (with path compression and union by rank):
- Find: O(α(n)) where α is inverse Ackermann function (nearly constant)
- Union: O(α(n))
"""

class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        """Find the root of the set containing x with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        """Union the sets containing x and y using union by rank."""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            # Union by rank
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x, y):
        """Check if x and y are in the same set."""
        return self.find(x) == self.find(y)

    def get_sets(self):
        """Get all current sets."""
        sets = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root not in sets:
                sets[root] = []
            sets[root].append(i)
        return list(sets.values())

    def __str__(self):
        return str(self.get_sets())


# Example usage and test cases
if __name__ == "__main__":
    ds = DisjointSet(10)

    # Initial sets: each element is its own set
    print("Initial sets:", ds)

    # Union operations
    ds.union(0, 1)
    ds.union(1, 2)
    ds.union(3, 4)
    ds.union(5, 6)
    ds.union(6, 7)
    ds.union(8, 9)

    print("After unions:", ds)

    # Check connections
    print("0 and 2 connected:", ds.connected(0, 2))  # True
    print("0 and 3 connected:", ds.connected(0, 3))  # False

    # More unions
    ds.union(2, 4)
    ds.union(7, 9)

    print("After more unions:", ds)
    print("0 and 3 connected:", ds.connected(0, 3))  # True
    print("5 and 8 connected:", ds.connected(5, 8))  # True
