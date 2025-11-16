"""
Fenwick Tree (Binary Indexed Tree) Implementation in Python

A Fenwick Tree is a data structure that provides efficient methods for:
- Prefix sum queries
- Point updates
- Range sum queries (with some modifications)

Time Complexities:
- Update: O(log n)
- Prefix Sum Query: O(log n)
- Range Sum Query: O(log n)
"""

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        """Update the value at index by delta."""
        index += 1  # 1-based indexing
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index  # Move to next index

    def prefix_sum(self, index):
        """Get the prefix sum from 0 to index."""
        index += 1  # 1-based indexing
        sum_val = 0
        while index > 0:
            sum_val += self.tree[index]
            index -= index & -index  # Move to parent
        return sum_val

    def range_sum(self, left, right):
        """Get the sum from left to right (inclusive)."""
        return self.prefix_sum(right) - self.prefix_sum(left - 1)

    def __str__(self):
        return str(self.tree[1:])  # Show 1-based values


# Example usage and test cases
if __name__ == "__main__":
    # Initialize with array [1, 2, 3, 4, 5]
    ft = FenwickTree(5)
    values = [1, 2, 3, 4, 5]
    for i, val in enumerate(values):
        ft.update(i, val)

    print("Fenwick Tree:", ft)

    # Prefix sums
    print("Prefix sum up to index 2:", ft.prefix_sum(2))  # 1+2+3=6
    print("Prefix sum up to index 4:", ft.prefix_sum(4))  # 1+2+3+4+5=15

    # Range sums
    print("Range sum [1, 3]:", ft.range_sum(1, 3))  # 2+3+4=9
    print("Range sum [0, 4]:", ft.range_sum(0, 4))  # 1+2+3+4+5=15

    # Update value at index 2 by +10 (original 3 becomes 13)
    ft.update(2, 10)
    print("After updating index 2 by +10:")
    print("Prefix sum up to index 2:", ft.prefix_sum(2))  # 1+2+13=16
    print("Range sum [1, 3]:", ft.range_sum(1, 3))  # 2+13+4=19
