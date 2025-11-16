"""
Linked List Implementations in Python

This module provides implementations of:
- Singly Linked List
- Doubly Linked List
- Circular Linked List

Time Complexities:
- Access: O(n)
- Insert/Delete at head: O(1)
- Insert/Delete at tail: O(1) for doubly, O(n) for singly
- Search: O(n)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Singly Linked List
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        """Append an element to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def prepend(self, data):
        """Prepend an element to the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def delete(self, data):
        """Delete the first occurrence of data."""
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next

    def search(self, data):
        """Search for data in the list."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)

# Doubly Linked List
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        """Append an element to the end of the list."""
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def prepend(self, data):
        """Prepend an element to the beginning of the list."""
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def delete(self, data):
        """Delete the first occurrence of data."""
        if not self.head:
            return
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self.size -= 1
                return
            current = current.next

    def search(self, data):
        """Search for data in the list."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " <-> ".join(elements)

# Circular Linked List
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        """Append an element to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
        self.size += 1

    def prepend(self, data):
        """Prepend an element to the beginning of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node
        self.size += 1

    def delete(self, data):
        """Delete the first occurrence of data."""
        if not self.head:
            return
        current = self.head
        prev = None
        while True:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    # Deleting head
                    if self.size == 1:
                        self.head = None
                    else:
                        # Find the last node
                        last = self.head
                        while last.next != self.head:
                            last = last.next
                        last.next = current.next
                        self.head = current.next
                self.size -= 1
                return
            prev = current
            current = current.next
            if current == self.head:
                break

    def search(self, data):
        """Search for data in the list."""
        if not self.head:
            return False
        current = self.head
        while True:
            if current.data == data:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def __str__(self):
        if not self.head:
            return ""
        elements = []
        current = self.head
        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        return " -> ".join(elements) + " -> (back to head)"


# Example usage and test cases
if __name__ == "__main__":
    # Singly Linked List
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    print("Singly Linked List:", sll)
    sll.prepend(0)
    print("After prepend 0:", sll)
    sll.delete(2)
    print("After delete 2:", sll)
    print("Search 3:", sll.search(3))

    # Doubly Linked List
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    print("Doubly Linked List:", dll)
    dll.prepend(0)
    print("After prepend 0:", dll)
    dll.delete(2)
    print("After delete 2:", dll)

    # Circular Linked List
    cll = CircularLinkedList()
    cll.append(1)
    cll.append(2)
    cll.append(3)
    print("Circular Linked List:", cll)
    cll.prepend(0)
    print("After prepend 0:", cll)
    cll.delete(2)
    print("After delete 2:", cll)
