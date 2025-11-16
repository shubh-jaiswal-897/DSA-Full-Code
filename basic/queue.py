"""
Queue Implementations in Python

This module provides implementations of:
1. Queue using Python list
2. Queue using linked list
3. Deque (Double-ended queue)
4. Priority Queue using heapq

Time Complexities:
- Enqueue: O(1) for list/ll, O(log n) for priority queue
- Dequeue: O(1) for list/ll, O(log n) for priority queue
- Peek: O(1)
"""

from basic.linked_list import Node
import heapq

# Queue using Python list
class ListQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return the front item."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.queue.pop(0)

    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.queue[0]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the size of the queue."""
        return len(self.queue)

    def __str__(self):
        return str(self.queue)

# Queue using linked list
class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def dequeue(self):
        """Remove and return the front item."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        item = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        self._size -= 1
        return item

    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.front.data

    def is_empty(self):
        """Check if the queue is empty."""
        return self.front is None

    def size(self):
        """Return the size of the queue."""
        return self._size

    def __str__(self):
        elements = []
        current = self.front
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)

# Deque (Double-ended queue)
class Deque:
    def __init__(self):
        self.deque = []

    def add_front(self, item):
        """Add an item to the front."""
        self.deque.insert(0, item)

    def add_rear(self, item):
        """Add an item to the rear."""
        self.deque.append(item)

    def remove_front(self):
        """Remove and return the front item."""
        if self.is_empty():
            raise IndexError("Remove from empty deque")
        return self.deque.pop(0)

    def remove_rear(self):
        """Remove and return the rear item."""
        if self.is_empty():
            raise IndexError("Remove from empty deque")
        return self.deque.pop()

    def peek_front(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty deque")
        return self.deque[0]

    def peek_rear(self):
        """Return the rear item without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty deque")
        return self.deque[-1]

    def is_empty(self):
        """Check if the deque is empty."""
        return len(self.deque) == 0

    def size(self):
        """Return the size of the deque."""
        return len(self.deque)

    def __str__(self):
        return str(self.deque)

# Priority Queue using heapq
class PriorityQueue:
    def __init__(self):
        self.heap = []
        self._size = 0

    def enqueue(self, item, priority=0):
        """Add an item with a priority."""
        heapq.heappush(self.heap, (priority, item))
        self._size += 1

    def dequeue(self):
        """Remove and return the item with the highest priority (lowest number)."""
        if self.is_empty():
            raise IndexError("Dequeue from empty priority queue")
        priority, item = heapq.heappop(self.heap)
        self._size -= 1
        return item

    def peek(self):
        """Return the item with the highest priority without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty priority queue")
        return self.heap[0][1]

    def is_empty(self):
        """Check if the priority queue is empty."""
        return len(self.heap) == 0

    def size(self):
        """Return the size of the priority queue."""
        return self._size

    def __str__(self):
        return str([(p, i) for p, i in self.heap])


# Example usage and test cases
if __name__ == "__main__":
    # List-based Queue
    list_queue = ListQueue()
    list_queue.enqueue(1)
    list_queue.enqueue(2)
    list_queue.enqueue(3)
    print("List Queue:", list_queue)
    print("Dequeue:", list_queue.dequeue())
    print("Peek:", list_queue.peek())
    print("Size:", list_queue.size())

    # Linked List-based Queue
    ll_queue = LinkedListQueue()
    ll_queue.enqueue(1)
    ll_queue.enqueue(2)
    ll_queue.enqueue(3)
    print("Linked List Queue:", ll_queue)
    print("Dequeue:", ll_queue.dequeue())
    print("Peek:", ll_queue.peek())

    # Deque
    deque = Deque()
    deque.add_front(1)
    deque.add_rear(2)
    deque.add_front(0)
    print("Deque:", deque)
    print("Remove front:", deque.remove_front())
    print("Remove rear:", deque.remove_rear())

    # Priority Queue
    pq = PriorityQueue()
    pq.enqueue("task1", 3)
    pq.enqueue("task2", 1)
    pq.enqueue("task3", 2)
    print("Priority Queue:", pq)
    print("Dequeue highest priority:", pq.dequeue())
    print("Peek:", pq.peek())
