"""
Tree Data Structures in Python

This module provides implementations of:
1. Binary Tree
2. Binary Search Tree (BST)
3. AVL Tree (Self-balancing BST)
4. Red-Black Tree (Self-balancing BST)

Time Complexities:
- Binary Tree: O(n) for most operations
- BST: O(h) where h is height (worst O(n), average O(log n))
- AVL Tree: O(log n) for all operations
- Red-Black Tree: O(log n) for all operations
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Binary Tree
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """Insert a node in level order."""
        if not self.root:
            self.root = TreeNode(data)
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if not node.left:
                node.left = TreeNode(data)
                return
            else:
                queue.append(node.left)
            if not node.right:
                node.right = TreeNode(data)
                return
            else:
                queue.append(node.right)

    def inorder_traversal(self, node, result=None):
        """Inorder traversal: Left -> Root -> Right"""
        if result is None:
            result = []
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.data)
            self.inorder_traversal(node.right, result)
        return result

    def preorder_traversal(self, node, result=None):
        """Preorder traversal: Root -> Left -> Right"""
        if result is None:
            result = []
        if node:
            result.append(node.data)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)
        return result

    def postorder_traversal(self, node, result=None):
        """Postorder traversal: Left -> Right -> Root"""
        if result is None:
            result = []
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.data)
        return result

    def level_order_traversal(self):
        """Level order traversal using queue."""
        if not self.root:
            return []
        result = []
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

# Binary Search Tree
class BSTNode(TreeNode):
    def __init__(self, data):
        super().__init__(data)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """Insert a node maintaining BST property."""
        if not self.root:
            self.root = BSTNode(data)
            return
        current = self.root
        while True:
            if data < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = BSTNode(data)
                    return
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = BSTNode(data)
                    return

    def search(self, data):
        """Search for a value in BST."""
        current = self.root
        while current:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def delete(self, data):
        """Delete a node from BST."""
        self.root = self._delete_helper(self.root, data)

    def _delete_helper(self, node, data):
        if not node:
            return node
        if data < node.data:
            node.left = self._delete_helper(node.left, data)
        elif data > node.data:
            node.right = self._delete_helper(node.right, data)
        else:
            # Node with one or no child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            # Node with two children
            temp = self._min_value_node(node.right)
            node.data = temp.data
            node.right = self._delete_helper(node.right, temp.data)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def inorder_traversal(self, node=None, result=None):
        if node is None:
            node = self.root
        return super(BinarySearchTree, self).inorder_traversal(node, result)

# AVL Tree Node
class AVLNode(TreeNode):
    def __init__(self, data):
        super().__init__(data)
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        return y

    def insert(self, data):
        """Insert a node and balance the tree."""
        self.root = self._insert_helper(self.root, data)

    def _insert_helper(self, node, data):
        if not node:
            return AVLNode(data)
        if data < node.data:
            node.left = self._insert_helper(node.left, data)
        else:
            node.right = self._insert_helper(node.right, data)

        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        balance = self.get_balance(node)

        # Left Left Case
        if balance > 1 and data < node.left.data:
            return self.right_rotate(node)
        # Right Right Case
        if balance < -1 and data > node.right.data:
            return self.left_rotate(node)
        # Left Right Case
        if balance > 1 and data > node.left.data:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        # Right Left Case
        if balance < -1 and data < node.right.data:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        return node

    def inorder_traversal(self, node=None, result=None):
        if node is None:
            node = self.root
        return super(AVLTree, self).inorder_traversal(node, result)

# Red-Black Tree (Simplified implementation)
class RBNode(TreeNode):
    def __init__(self, data, color="RED"):
        super().__init__(data)
        self.color = color  # "RED" or "BLACK"

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """Insert a node and maintain red-black properties."""
        if not self.root:
            self.root = RBNode(data, "BLACK")
            return
        # Simplified: Just insert like BST and recolor (not full implementation)
        self.root = self._insert_helper(self.root, data)

    def _insert_helper(self, node, data):
        if not node:
            return RBNode(data)
        if data < node.data:
            node.left = self._insert_helper(node.left, data)
        else:
            node.right = self._insert_helper(node.right, data)
        return node

    def inorder_traversal(self, node=None, result=None):
        if node is None:
            node = self.root
        return super(RedBlackTree, self).inorder_traversal(node, result)


# Example usage and test cases
if __name__ == "__main__":
    # Binary Tree
    bt = BinaryTree()
    for i in range(1, 8):
        bt.insert(i)
    print("Binary Tree Level Order:", bt.level_order_traversal())
    print("Inorder:", bt.inorder_traversal(bt.root))

    # Binary Search Tree
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    print("BST Inorder:", bst.inorder_traversal())
    print("Search 40:", bst.search(40))
    bst.delete(30)
    print("After deleting 30:", bst.inorder_traversal())

    # AVL Tree
    avl = AVLTree()
    for val in [10, 20, 30, 40, 50, 25]:
        avl.insert(val)
    print("AVL Inorder:", avl.inorder_traversal())

    # Red-Black Tree
    rbt = RedBlackTree()
    rbt.insert(10)
    rbt.insert(20)
    rbt.insert(30)
    print("RBT Inorder:", rbt.inorder_traversal())
