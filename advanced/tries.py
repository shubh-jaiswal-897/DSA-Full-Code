"""
Trie (Prefix Tree) Implementation in Python

A Trie is a tree-like data structure used for efficient retrieval of keys in a dataset of strings.
Common applications include autocomplete and spell checking.

Time Complexities:
- Insert: O(m) where m is key length
- Search: O(m)
- Delete: O(m)
- Starts with: O(m)
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert a word into the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        """Search for a complete word in the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        """Check if any word starts with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word):
        """Delete a word from the trie."""
        def _delete_helper(node, word, index):
            if index == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0

            char = word[index]
            if char not in node.children:
                return False

            should_delete = _delete_helper(node.children[char], word, index + 1)

            if should_delete:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word
            else:
                return False

        return _delete_helper(self.root, word, 0)

    def get_all_words(self):
        """Get all words stored in the trie."""
        result = []
        def dfs(node, current_word):
            if node.is_end_of_word:
                result.append(current_word)
            for char, child in node.children.items():
                dfs(child, current_word + char)
        dfs(self.root, "")
        return result

    def autocomplete(self, prefix):
        """Return all words that start with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        result = []
        def dfs(current_node, current_word):
            if current_node.is_end_of_word:
                result.append(prefix + current_word)
            for char, child in current_node.children.items():
                dfs(child, current_word + char)
        dfs(node, "")
        return result

    def __str__(self):
        return str(self.get_all_words())


# Example usage and test cases
if __name__ == "__main__":
    trie = Trie()

    # Insert words
    words = ["apple", "app", "application", "bat", "ball", "cat"]
    for word in words:
        trie.insert(word)

    print("All words in trie:", trie.get_all_words())

    # Search
    print("Search 'apple':", trie.search("apple"))
    print("Search 'appl':", trie.search("appl"))
    print("Search 'dog':", trie.search("dog"))

    # Starts with
    print("Starts with 'app':", trie.starts_with("app"))
    print("Starts with 'ba':", trie.starts_with("ba"))
    print("Starts with 'dog':", trie.starts_with("dog"))

    # Autocomplete
    print("Autocomplete 'app':", trie.autocomplete("app"))
    print("Autocomplete 'b':", trie.autocomplete("b"))

    # Delete
    trie.delete("apple")
    print("After deleting 'apple':", trie.get_all_words())
    print("Search 'apple' after delete:", trie.search("apple"))
    print("Search 'app' after delete:", trie.search("app"))  # Should still exist
