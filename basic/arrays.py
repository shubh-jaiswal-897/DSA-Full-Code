"""
Dynamic Array Implementation in Python

This module provides a basic dynamic array implementation using Python lists.
Dynamic arrays automatically resize when elements are added or removed.

Time Complexities:
- Access: O(1)
- Append: O(1) amortized
- Insert/Delete: O(n)
"""

class DynamicArray:
    def __init__(self):
        self.array = []
        self.size = 0

    def append(self, value):
        """Append an element to the end of the array."""
        self.array.append(value)
        self.size += 1

    def insert(self, index, value):
        """Insert an element at a specific index."""
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        self.array.insert(index, value)
        self.size += 1

    def delete(self, index):
        """Delete an element at a specific index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        self.array.pop(index)
        self.size -= 1

    def get(self, index):
        """Get an element at a specific index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.array[index]

    def set(self, index, value):
        """Set an element at a specific index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        self.array[index] = value

    def __len__(self):
        return self.size

    def __str__(self):
        return str(self.array)


# Example usage and test cases
if __name__ == "__main__":
    arr = DynamicArray()
    arr.append(1)
    arr.append(2)
    arr.append(3)
    print("Array after appends:", arr)  # [1, 2, 3]

    arr.insert(1, 10)
    print("Array after insert at index 1:", arr)  # [1, 10, 2, 3]

    arr.delete(2)
    print("Array after delete at index 2:", arr)  # [1, 10, 3]

    print("Element at index 1:", arr.get(1))  # 10

    arr.set(0, 5)
    print("Array after set index 0 to 5:", arr)  # [5, 10, 3]
