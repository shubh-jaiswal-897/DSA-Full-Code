"""
Median Finder Implementation in Python

Find the median of a stream of numbers using two heaps:
- Max-heap for lower half
- Min-heap for upper half

Time Complexities:
- Add number: O(log n)
- Find median: O(1)
"""

import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = []  # For lower half (negated values)
        self.min_heap = []  # For upper half

    def add_num(self, num):
        """Add a number to the data structure."""
        # Add to max_heap (lower half)
        heapq.heappush(self.max_heap, -num)

        # Balance: move largest from lower to upper
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # Ensure max_heap has at most one more element than min_heap
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self):
        """Find the median of all numbers added so far."""
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2

# Example usage and test cases
if __name__ == "__main__":
    mf = MedianFinder()

    nums = [1, 2, 3, 4, 5]
    for num in nums:
        mf.add_num(num)
        print(f"Added {num}, median: {mf.find_median()}")

    # Additional test
    mf2 = MedianFinder()
    mf2.add_num(5)
    print("Median after 5:", mf2.find_median())  # 5
    mf2.add_num(10)
    print("Median after 5,10:", mf2.find_median())  # 7.5
    mf2.add_num(3)
    print("Median after 5,10,3:", mf2.find_median())  # 5
