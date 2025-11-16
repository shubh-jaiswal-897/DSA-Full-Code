"""
LRU Cache Implementation in Python

LRU (Least Recently Used) Cache is a cache replacement policy that removes the least recently used item when the cache is full.

Time Complexities:
- Get: O(1)
- Put: O(1)
"""

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """Get the value of key if it exists, otherwise return -1."""
        if key not in self.cache:
            return -1
        # Move to end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        """Set or insert the value if the key is not already present."""
        if key in self.cache:
            # Update value and move to end
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                # Remove least recently used (first item)
                self.cache.popitem(last=False)
            self.cache[key] = value

    def __str__(self):
        return str(dict(self.cache))


# Example usage and test cases
if __name__ == "__main__":
    lru = LRUCache(3)

    lru.put(1, 1)
    lru.put(2, 2)
    lru.put(3, 3)
    print("Cache:", lru)  # {1: 1, 2: 2, 3: 3}

    print("Get 1:", lru.get(1))  # 1, now 1 is most recent
    print("Cache:", lru)  # {2: 2, 3: 3, 1: 1}

    lru.put(4, 4)  # Evicts 2 (least recently used)
    print("Cache after put 4:", lru)  # {3: 3, 1: 1, 4: 4}

    print("Get 2:", lru.get(2))  # -1 (not found)
    print("Get 3:", lru.get(3))  # 3, now 3 is most recent
    print("Cache:", lru)  # {1: 1, 4: 4, 3: 3}
