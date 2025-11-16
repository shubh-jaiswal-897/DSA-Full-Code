"""
Stack Implementations in Python

This module provides two stack implementations:
1. Stack using Python list
2. Stack using linked list

Time Complexities:
- Push: O(1)
- Pop: O(1)
- Peek: O(1)
- Search: O(n)
"""

from basic.linked_list import Node

# Stack using Python list
class ListStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Push an item onto the stack."""
        self.stack.append(item)

    def pop(self):
        """Pop an item from the stack."""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.stack.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.stack[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the size of the stack."""
        return len(self.stack)

    def __str__(self):
        return str(self.stack)

# Stack using linked list
class LinkedListStack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, item):
        """Push an item onto the stack."""
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        """Pop an item from the stack."""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        item = self.top.data
        self.top = self.top.next
        self._size -= 1
        return item

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.data

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None

    def size(self):
        """Return the size of the stack."""
        return self._size

    def __str__(self):
        elements = []
        current = self.top
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)


# Example usage and test cases
if __name__ == "__main__":
    # List-based Stack
    list_stack = ListStack()
    list_stack.push(1)
    list_stack.push(2)
    list_stack.push(3)
    print("List Stack:", list_stack)
    print("Peek:", list_stack.peek())
    print("Pop:", list_stack.pop())
    print("After pop:", list_stack)
    print("Size:", list_stack.size())

    # Linked List-based Stack
    ll_stack = LinkedListStack()
    ll_stack.push(1)
    ll_stack.push(2)
    ll_stack.push(3)
    print("Linked List Stack:", ll_stack)
    print("Peek:", ll_stack.peek())
    print("Pop:", ll_stack.pop())
    print("After pop:", ll_stack)
    print("Size:", ll_stack.size())
