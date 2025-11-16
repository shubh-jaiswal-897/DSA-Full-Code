"""
Segment Tree Implementation in Python

A Segment Tree is a data structure for efficient range queries and updates.
It supports range minimum/maximum queries, range sum queries, etc.

Time Complexities:
- Build: O(n)
- Update: O(log n)
- Query: O(log n)
"""

class SegmentTree:
    def __init__(self, arr, func=min):
        """
        Initialize segment tree.
        func: min, max, sum, etc.
        """
        self.func = func
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        """Build the segment tree."""
        if start == end:
            self.tree[node] = arr[start]
            return
        mid = (start + end) // 2
        self.build(arr, 2*node+1, start, mid)
        self.build(arr, 2*node+2, mid+1, end)
        self.tree[node] = self.func(self.tree[2*node+1], self.tree[2*node+2])

    def update(self, node, start, end, idx, val):
        """Update value at index idx to val."""
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2*node+1, start, mid, idx, val)
        else:
            self.update(2*node+2, mid+1, end, idx, val)
        self.tree[node] = self.func(self.tree[2*node+1], self.tree[2*node+2])

    def query(self, node, start, end, l, r):
        """Query the range [l, r]."""
        if r < start or end < l:
            return float('inf') if self.func == min else float('-inf')
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        left = self.query(2*node+1, start, mid, l, r)
        right = self.query(2*node+2, mid+1, end, l, r)
        if left == float('inf') or left == float('-inf'):
            return right
        if right == float('inf') or right == float('-inf'):
            return left
        return self.func(left, right)

    def update_value(self, idx, val):
        """Public method to update value at index."""
        self.update(0, 0, self.n-1, idx, val)

    def range_query(self, l, r):
        """Public method to query range [l, r]."""
        return self.query(0, 0, self.n-1, l, r)

# Sum Segment Tree
class SumSegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
            return
        mid = (start + end) // 2
        self.build(arr, 2*node+1, start, mid)
        self.build(arr, 2*node+2, mid+1, end)
        self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2*node+1, start, mid, idx, val)
        else:
            self.update(2*node+2, mid+1, end, idx, val)
        self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        left = self.query(2*node+1, start, mid, l, r)
        right = self.query(2*node+2, mid+1, end, l, r)
        return left + right

    def update_value(self, idx, val):
        self.update(0, 0, self.n-1, idx, val)

    def range_sum(self, l, r):
        return self.query(0, 0, self.n-1, l, r)


# Example usage and test cases
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]

    # Min Segment Tree
    min_st = SegmentTree(arr, min)
    print("Min in range [1, 3]:", min_st.range_query(1, 3))  # 3
    min_st.update_value(2, 2)
    print("Min in range [1, 3] after update:", min_st.range_query(1, 3))  # 2

    # Max Segment Tree
    max_st = SegmentTree(arr, max)
    print("Max in range [0, 4]:", max_st.range_query(0, 4))  # 9

    # Sum Segment Tree
    sum_st = SumSegmentTree(arr)
    print("Sum in range [1, 4]:", sum_st.range_sum(1, 4))  # 3+5+7+9=24
    sum_st.update_value(1, 10)
    print("Sum in range [1, 4] after update:", sum_st.range_sum(1, 4))  # 10+5+7+9=31
