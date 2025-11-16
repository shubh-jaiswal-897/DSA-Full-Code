"""
Heap Data Structures in Python

This module provides implementations of:
1. Min-Heap
2. Max-Heap

Time Complexities:
- Insert: O(log n)
- Extract Min/Max: O(log n)
- Peek: O(1)
- Heapify: O(log n)
"""

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify_up(self, index):
        """Bubble up the element at index to maintain heap property."""
        while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def heapify_down(self, index):
        """Bubble down the element at index to maintain heap property."""
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.swap(index, smallest)
            self.heapify_down(smallest)

    def insert(self, value):
        """Insert a value into the heap."""
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def extract_min(self):
        """Extract and return the minimum value."""
        if not self.heap:
            raise IndexError("Extract from empty heap")
        if len(self.heap) == 1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return min_val

    def peek(self):
        """Return the minimum value without removing it."""
        if not self.heap:
            raise IndexError("Peek from empty heap")
        return self.heap[0]

    def is_empty(self):
        """Check if the heap is empty."""
        return len(self.heap) == 0

    def size(self):
        """Return the size of the heap."""
        return len(self.heap)

    def __str__(self):
        return str(self.heap)

class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify_up(self, index):
        """Bubble up the element at index to maintain heap property."""
        while index > 0 and self.heap[index] > self.heap[self.parent(index)]:
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def heapify_down(self, index):
        """Bubble down the element at index to maintain heap property."""
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.swap(index, largest)
            self.heapify_down(largest)

    def insert(self, value):
        """Insert a value into the heap."""
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def extract_max(self):
        """Extract and return the maximum value."""
        if not self.heap:
            raise IndexError("Extract from empty heap")
        if len(self.heap) == 1:
            return self.heap.pop()
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return max_val

    def peek(self):
        """Return the maximum value without removing it."""
        if not self.heap:
            raise IndexError("Peek from empty heap")
        return self.heap[0]

    def is_empty(self):
        """Check if the heap is empty."""
        return len(self.heap) == 0

    def size(self):
        """Return the size of the heap."""
        return len(self.heap)

    def __str__(self):
        return str(self.heap)


# Example usage and test cases
if __name__ == "__main__":
    # Min-Heap
    min_heap = MinHeap()
    min_heap.insert(10)
    min_heap.insert(5)
    min_heap.insert(15)
    min_heap.insert(3)
    print("Min-Heap:", min_heap)
    print("Extract Min:", min_heap.extract_min())
    print("After extract:", min_heap)
    print("Peek:", min_heap.peek())

    # Max-Heap
    max_heap = MaxHeap()
    max_heap.insert(10)
    max_heap.insert(5)
    max_heap.insert(15)
    max_heap.insert(3)
    print("Max-Heap:", max_heap)
    print("Extract Max:", max_heap.extract_max())
    print("After extract:", max_heap)
    print("Peek:", max_heap.peek())
