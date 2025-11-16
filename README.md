# Python Data Structures Repository

This repository contains comprehensive implementations of various data structures and algorithms in Python, from basic to advanced levels, including interview-level problems.

## Repository Structure

```
├── basic/
│   ├── arrays.py          # Dynamic arrays using lists
│   ├── linked_list.py     # Singly, doubly, circular linked lists
│   ├── stack.py           # Stack with list and linked list implementations
│   ├── queue.py           # Queue, deque, priority queue
│   └── hash_table.py      # Hash table with chaining/open addressing
├── advanced/
│   ├── trees.py           # Binary tree, BST, AVL tree, red-black tree
│   ├── heaps.py           # Min-heap, max-heap
│   ├── graphs.py          # Graph representations, DFS, BFS, shortest paths
│   ├── tries.py           # Trie (prefix tree)
│   ├── segment_tree.py    # Segment tree for range queries
│   ├── fenwick_tree.py    # Fenwick tree (binary indexed tree)
│   └── disjoint_set.py    # Union-Find with path compression
├── interview_problems/
│   ├── lru_cache.py       # LRU cache implementation
│   ├── two_sum.py         # Two sum with hash table
│   ├── median_finder.py   # Median finder using heaps
│   ├── valid_parentheses.py # Valid parentheses using stack
│   ├── clone_graph.py     # Clone graph using DFS/BFS
│   └── word_ladder.py     # Word ladder using BFS
├── TODO.md                # Task tracking
└── README.md              # This file
```

## Data Structures Overview

### Basic Data Structures
- **Arrays**: Dynamic arrays with basic operations (append, insert, delete, get, set)
- **Linked Lists**: Singly, doubly, and circular linked list implementations
- **Stacks**: Stack implementations using lists and linked lists
- **Queues**: Queue, deque, and priority queue implementations
- **Hash Tables**: Hash tables with chaining and open addressing collision resolution

### Advanced Data Structures
- **Trees**: Binary trees, binary search trees (BST), AVL trees, red-black trees
- **Heaps**: Min-heap and max-heap implementations
- **Graphs**: Graph representations, DFS, BFS, Dijkstra's and Bellman-Ford algorithms
- **Tries**: Prefix tree for efficient string operations
- **Segment Trees**: For range queries and updates
- **Fenwick Trees**: Binary indexed trees for prefix sum queries
- **Disjoint Sets**: Union-Find with path compression and union by rank

### Interview Problems
- **LRU Cache**: Least recently used cache implementation
- **Two Sum**: Find two numbers that add up to a target
- **Median Finder**: Find median in a stream of numbers using heaps
- **Valid Parentheses**: Check for valid bracket sequences
- **Clone Graph**: Deep copy of a graph using DFS
- **Word Ladder**: Shortest transformation sequence using BFS

## Usage

Each file contains:
- Class definitions with key methods
- Time and space complexity analysis in comments
- Example usage and test cases in the `if __name__ == "__main__":` block

To run any implementation, simply execute the Python file:

```bash
python basic/stack.py
python advanced/graphs.py
python interview_problems/two_sum.py
```

## Time Complexities Summary

| Data Structure | Operation | Time Complexity |
|----------------|-----------|-----------------|
| Array | Access | O(1) |
| Array | Insert/Delete | O(n) |
| Linked List | Access | O(n) |
| Linked List | Insert/Delete | O(1) |
| Stack/Queue | Push/Pop | O(1) |
| Hash Table | Insert/Search/Delete | O(1) average |
| BST | Search/Insert/Delete | O(log n) average |
| AVL Tree | All operations | O(log n) |
| Heap | Insert/Extract | O(log n) |
| Graph Traversal | DFS/BFS | O(V + E) |
| Dijkstra | Shortest path | O((V + E) log V) |
| Trie | Insert/Search | O(m) |
| Segment Tree | Query/Update | O(log n) |
| Fenwick Tree | Update/Query | O(log n) |
| Disjoint Set | Find/Union | O(α(n)) |

## Contributing

Feel free to contribute by:
- Adding more data structures
- Improving existing implementations
- Adding more test cases
- Fixing bugs

## License

This repository is for educational purposes. Feel free to use and modify the code as needed.
