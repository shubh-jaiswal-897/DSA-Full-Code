"""
Hash Table Implementations in Python

This module provides two hash table implementations:
1. Hash Table with Chaining (using linked lists)
2. Hash Table with Open Addressing (Linear Probing)

Time Complexities (average case):
- Insert: O(1)
- Delete: O(1)
- Search: O(1)
Worst case: O(n) for chaining, O(n) for open addressing
"""

from basic.linked_list import Node

# Hash Table with Chaining
class ChainingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.count = 0

    def _hash(self, key):
        """Simple hash function."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair."""
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = Node((key, value))
        else:
            current = self.table[index]
            while current:
                if current.data[0] == key:
                    current.data = (key, value)  # Update value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = Node((key, value))
        self.count += 1

    def search(self, key):
        """Search for a key and return its value."""
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.data[0] == key:
                return current.data[1]
            current = current.next
        return None

    def delete(self, key):
        """Delete a key-value pair."""
        index = self._hash(key)
        current = self.table[index]
        prev = None
        while current:
            if current.data[0] == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                self.count -= 1
                return True
            prev = current
            current = current.next
        return False

    def __str__(self):
        result = []
        for i, head in enumerate(self.table):
            if head:
                chain = []
                current = head
                while current:
                    chain.append(f"{current.data[0]}:{current.data[1]}")
                    current = current.next
                result.append(f"[{i}]: {' -> '.join(chain)}")
        return "\n".join(result)

# Hash Table with Open Addressing (Linear Probing)
class OpenAddressingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.count = 0

    def _hash(self, key):
        """Simple hash function."""
        return hash(key) % self.size

    def _probe(self, index, i):
        """Linear probing."""
        return (index + i) % self.size

    def insert(self, key, value):
        """Insert a key-value pair."""
        if self.count >= self.size:
            raise Exception("Hash table is full")
        index = self._hash(key)
        i = 0
        while i < self.size:
            probe_index = self._probe(index, i)
            if self.table[probe_index] is None or self.table[probe_index][0] == "DELETED":
                self.table[probe_index] = (key, value)
                self.count += 1
                return
            elif self.table[probe_index][0] == key:
                self.table[probe_index] = (key, value)  # Update value
                return
            i += 1
        raise Exception("Could not insert, table full")

    def search(self, key):
        """Search for a key and return its value."""
        index = self._hash(key)
        i = 0
        while i < self.size:
            probe_index = self._probe(index, i)
            if self.table[probe_index] is None:
                return None
            if self.table[probe_index][0] == key:
                return self.table[probe_index][1]
            i += 1
        return None

    def delete(self, key):
        """Delete a key-value pair (lazy deletion)."""
        index = self._hash(key)
        i = 0
        while i < self.size:
            probe_index = self._probe(index, i)
            if self.table[probe_index] is None:
                return False
            if self.table[probe_index][0] == key:
                self.table[probe_index] = ("DELETED", None)
                self.count -= 1
                return True
            i += 1
        return False

    def __str__(self):
        result = []
        for i, entry in enumerate(self.table):
            if entry and entry[0] != "DELETED":
                result.append(f"[{i}]: {entry[0]}:{entry[1]}")
            elif entry and entry[0] == "DELETED":
                result.append(f"[{i}]: DELETED")
        return "\n".join(result)


# Example usage and test cases
if __name__ == "__main__":
    # Chaining Hash Table
    chaining_ht = ChainingHashTable(5)
    chaining_ht.insert("apple", 10)
    chaining_ht.insert("banana", 20)
    chaining_ht.insert("cherry", 30)
    chaining_ht.insert("date", 40)  # Collision with apple
    print("Chaining Hash Table:")
    print(chaining_ht)
    print("Search 'banana':", chaining_ht.search("banana"))
    chaining_ht.delete("banana")
    print("After deleting 'banana':")
    print(chaining_ht)

    # Open Addressing Hash Table
    open_ht = OpenAddressingHashTable(5)
    open_ht.insert("apple", 10)
    open_ht.insert("banana", 20)
    open_ht.insert("cherry", 30)
    open_ht.insert("date", 40)  # Probing
    print("\nOpen Addressing Hash Table:")
    print(open_ht)
    print("Search 'cherry':", open_ht.search("cherry"))
    open_ht.delete("cherry")
    print("After deleting 'cherry':")
    print(open_ht)
