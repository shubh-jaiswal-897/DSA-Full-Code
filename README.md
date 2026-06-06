# Data Structures and Algorithms (DSA) - Complete Implementation Guide

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Objectives](#objectives)
- [Technical Architecture](#technical-architecture)
- [Repository Structure](#repository-structure)
- [Data Structures Implemented](#data-structures-implemented)
- [Algorithms & Complexity Analysis](#algorithms--complexity-analysis)
- [Installation & Setup](#installation--setup)
- [Usage Examples](#usage-examples)
- [Learning Outcomes](#learning-outcomes)
- [Performance Benchmarks](#performance-benchmarks)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Project Overview

This comprehensive repository provides production-grade implementations of fundamental and advanced data structures and algorithms in Python. Designed for computer science students, coding interview aspirants, and software engineers seeking to deepen their understanding of algorithmic efficiency and computational complexity.

**Project Type:** Educational | Computer Science | Algorithm Design | Interview Preparation

---

## 🔍 Objectives

1. **Primary Objective:** Provide clear, well-documented implementations of essential data structures and algorithms
2. **Secondary Objectives:**
   - Demonstrate Time and Space complexity analysis for each data structure
   - Create reusable, production-ready code with comprehensive documentation
   - Facilitate interview preparation for FAANG companies
   - Enable hands-on learning of computational fundamentals
   - Support both academic and professional development

---

## 🏗️ Technical Architecture

### Technology Stack
- **Language:** Python 3.8+
- **Testing Framework:** unittest / pytest
- **Documentation:** Docstrings & Comments
- **Version Control:** Git

### Core Components
```
┌──────────────────────────────────┐
│   Basic Data Structures           │
│  (Arrays, Lists, Stacks, Queues) │
└──────────────┬───────────────────┘
               │
┌──────────────▼───────────────────┐
│   Advanced Data Structures        │
│  (Trees, Graphs, Heaps, Tries)   │
└──────────────┬───────────────────┘
               │
┌──────────────▼───────────────────┐
│   Algorithms & Problem Solving    │
│  (Sorting, Searching, DFS, BFS)  │
└──────────────┬───────────────────┘
               │
┌──────────────▼───────────────────┐
│   Interview-Level Problems        │
│  (LRU Cache, Median Finder, etc)  │
└──────────────────────────────────┘
```

---

## 📁 Repository Structure

```
DSA-Full-Code/
├── basic/
│   ├── arrays.py                 # Dynamic arrays, list operations
│   ├── linked_list.py           # Singly, doubly, circular linked lists
│   ├── stack.py                 # Stack implementations (array & linked list)
│   ├── queue.py                 # Queue, deque, priority queue
│   └── hash_table.py            # Hash tables with collision resolution
│
├── advanced/
│   ├── trees.py                 # Binary trees, BST, AVL, Red-Black trees
│   ├── heaps.py                 # Min-heap, max-heap, heap operations
│   ├── graphs.py                # Graph representations, traversals
│   ├── tries.py                 # Trie/Prefix tree implementations
│   ├── segment_tree.py          # Segment tree for range queries
│   ├── fenwick_tree.py          # Fenwick tree (binary indexed tree)
│   └── disjoint_set.py          # Union-Find with optimizations
│
├── interview_problems/
│   ├── lru_cache.py             # LRU cache using OrderedDict
│   ├── two_sum.py               # Two sum problem with hash table
│   ├── median_finder.py         # Median finder using two heaps
│   ├── valid_parentheses.py     # Bracket matching with stack
│   ├── clone_graph.py           # Graph deep copy with DFS/BFS
│   └── word_ladder.py           # BFS shortest path transformation
│
├── TODO.md                      # Development roadmap
└── README.md                    # This file
```

---

## 📊 Data Structures Implemented

### Basic Data Structures

#### 1. **Arrays & Lists**
- Dynamic array resizing
- Insert, delete, search operations
- Index-based access
- **Use Cases:** Storing ordered collections, random access

#### 2. **Linked Lists**
- Singly linked list
- Doubly linked list
- Circular linked list
- **Use Cases:** Dynamic memory allocation, insertion/deletion in middle

#### 3. **Stacks**
- Array-based implementation
- Linked list-based implementation
- Applications: function call stack, undo/redo, expression evaluation
- **Time Complexity:** O(1) for push/pop operations

#### 4. **Queues**
- Simple queue (FIFO)
- Deque (double-ended queue)
- Priority queue
- **Use Cases:** Task scheduling, BFS, load balancing

#### 5. **Hash Tables**
- Chaining collision resolution
- Open addressing collision resolution
- Load factor management
- **Average Time Complexity:** O(1) for insert/search/delete

---

### Advanced Data Structures

#### 1. **Trees**
- **Binary Trees:** Node-based tree structure
- **Binary Search Trees (BST):** Ordered binary trees
- **AVL Trees:** Self-balancing BST with height balance
- **Red-Black Trees:** Self-balancing BST with color properties
- **Operations:** Insert, delete, search, traversal (inorder, preorder, postorder)

#### 2. **Heaps**
- Min-heap and Max-heap implementations
- Heap sort algorithm
- Priority queue applications
- **Time Complexity:** O(log n) for insert/extract operations

#### 3. **Graphs**
- Adjacency matrix representation
- Adjacency list representation
- **Traversals:** DFS (Depth-First Search), BFS (Breadth-First Search)
- **Shortest Path Algorithms:** Dijkstra's, Bellman-Ford
- **Applications:** Social networks, GPS navigation, recommendation systems

#### 4. **Tries (Prefix Trees)**
- Character-based tree structure
- Insert, search, delete operations
- Autocomplete functionality
- **Time Complexity:** O(m) where m is word length

#### 5. **Segment Trees**
- Range query and point update
- Range update and point query
- **Applications:** Range minimum/maximum queries
- **Time Complexity:** O(log n) per operation

#### 6. **Fenwick Trees (Binary Indexed Trees)**
- Prefix sum queries
- Efficient range sum updates
- **Applications:** Inversion count, coordinate compression
- **Time Complexity:** O(log n) per operation

#### 7. **Disjoint Sets (Union-Find)**
- Union by rank optimization
- Path compression optimization
- **Applications:** Connected components, cycle detection
- **Time Complexity:** Nearly O(1) with optimizations

---

## 🔬 Algorithms & Complexity Analysis

### Comprehensive Complexity Table

| Data Structure | Operation | Time (Avg) | Time (Worst) | Space |
|---|---|---|---|---|
| **Array** | Access | O(1) | O(1) | O(n) |
| **Array** | Search | O(n) | O(n) | O(1) |
| **Array** | Insert | O(n) | O(n) | O(1) |
| **Array** | Delete | O(n) | O(n) | O(1) |
| **Linked List** | Access | O(n) | O(n) | O(1) |
| **Linked List** | Search | O(n) | O(n) | O(1) |
| **Linked List** | Insert | O(1) | O(1) | O(1) |
| **Linked List** | Delete | O(1) | O(1) | O(1) |
| **Stack** | Push/Pop | O(1) | O(1) | O(n) |
| **Queue** | Enqueue/Dequeue | O(1) | O(1) | O(n) |
| **Hash Table** | Insert/Search/Delete | O(1) | O(n) | O(n) |
| **BST** | Search/Insert/Delete | O(log n) | O(n) | O(n) |
| **AVL Tree** | Search/Insert/Delete | O(log n) | O(log n) | O(n) |
| **Heap** | Insert/Extract | O(log n) | O(log n) | O(n) |
| **Graph (BFS/DFS)** | Traversal | O(V+E) | O(V+E) | O(V) |
| **Dijkstra** | Shortest Path | O((V+E)logV) | O(V²) | O(V) |
| **Trie** | Insert/Search | O(m) | O(m) | O(k) |
| **Segment Tree** | Query/Update | O(log n) | O(log n) | O(n) |
| **Fenwick Tree** | Query/Update | O(log n) | O(log n) | O(n) |
| **Union-Find** | Find/Union | O(α(n)) | O(α(n)) | O(n) |

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git for version control

### Step 1: Clone Repository
```bash
git clone https://github.com/shubh-jaiswal-897/DSA-Full-Code.git
cd DSA-Full-Code
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: (Optional) Install Testing Framework
```bash
pip install pytest
```

---

## 🚀 Usage Examples

### Basic Data Structure Usage

#### Stack Example
```python
from basic.stack import Stack

# Create a stack
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())  # Output: 30
print(stack.peek()) # Output: 20
```

#### Linked List Example
```python
from basic.linked_list import LinkedList

# Create a linked list
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)

ll.display()  # Output: 1 -> 2 -> 3
```

#### Hash Table Example
```python
from basic.hash_table import HashTable

# Create a hash table
ht = HashTable()
ht.insert("name", "Shubh")
ht.insert("age", 22)

print(ht.search("name"))  # Output: Shubh
```

---

### Advanced Data Structure Usage

#### Binary Search Tree Example
```python
from advanced.trees import BST

# Create a BST
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(70)

print(bst.search(30))  # Output: True
print(bst.inorder())   # Output: [30, 50, 70]
```

#### Graph Traversal Example
```python
from advanced.graphs import Graph

# Create a graph
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)

print(graph.dfs(0))    # Depth-First Search
print(graph.bfs(0))    # Breadth-First Search
```

#### Heap Example
```python
from advanced.heaps import MinHeap

# Create a min heap
heap = MinHeap()
heap.insert(10)
heap.insert(5)
heap.insert(15)

print(heap.extract_min())  # Output: 5
```

---

### Interview Problems

#### LRU Cache Example
```python
from interview_problems.lru_cache import LRUCache

# Create LRU cache with capacity 2
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # Output: 1
cache.put(3, 3)      # Evicts key 2
print(cache.get(2))  # Output: -1 (not found)
```

#### Median Finder Example
```python
from interview_problems.median_finder import MedianFinder

mf = MedianFinder()
mf.addNum(1)
print(mf.findMedian())  # Output: 1.0
mf.addNum(2)
print(mf.findMedian())  # Output: 1.5
mf.addNum(3)
print(mf.findMedian())  # Output: 2.0
```

---

## 🎓 Learning Outcomes

After studying this repository, you will understand:

✅ **Fundamental Concepts:**
- How data structures organize and store information
- Time and space complexity analysis (Big O notation)
- Trade-offs between different data structures

✅ **Practical Applications:**
- When to use which data structure for specific problems
- Real-world use cases for each data structure
- Performance optimization techniques

✅ **Interview Preparation:**
- Common DSA problems and solutions
- Optimal approaches for algorithmic problems
- Code optimization strategies

✅ **Algorithm Design:**
- Algorithmic paradigms (greedy, divide-and-conquer, dynamic programming)
- Graph algorithms and shortest path problems
- Search and sorting techniques

---

## 📈 Performance Benchmarks

### Comparative Analysis

| Operation | Array | Linked List | BST | AVL Tree | Hash Table |
|-----------|-------|------------|-----|---------|-----------|
| Search | O(n) | O(n) | O(log n)* | O(log n) | O(1)* |
| Insert | O(n) | O(1) | O(log n)* | O(log n) | O(1)* |
| Delete | O(n) | O(1) | O(log n)* | O(log n) | O(1)* |
| Space | O(n) | O(n) | O(n) | O(n) | O(n) |

*Average case; worst case may differ

---

## 🤝 Contributing

Contributions are welcome and appreciated!

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/NewDS`)
3. **Add** new data structures with:
   - Clean, documented code
   - Time/space complexity analysis
   - Example usage
   - Unit tests
4. **Commit** your changes (`git commit -m 'Add NewDS implementation'`)
5. **Push** to the branch (`git push origin feature/NewDS`)
6. **Open** a Pull Request

### Guidelines
- Follow PEP 8 style guidelines
- Include comprehensive docstrings
- Add example test cases
- Document complexity analysis

---

## 📚 References & Resources

- **Books:**
  - "Introduction to Algorithms" - CLRS
  - "Cracking the Coding Interview" - Gayle Laakmann McDowell
  - "Data Structures and Algorithms in Python" - Goodrich, Tamassia, Goldwasser

- **Online Resources:**
  - LeetCode: Practice problems
  - GeeksforGeeks: Tutorials and articles
  - Visualgo.net: Algorithm visualizations

---

## 📄 License

This project is open source and available under the MIT License. Free to use, modify, and distribute for educational and commercial purposes.

---

## 📞 Contact & Support

**Author:** Shubh Jaiswal  
**GitHub:** [@shubh-jaiswal-897](https://github.com/shubh-jaiswal-897)  
**Email:** sj7518378908@gmail.com  

For questions, issues, or suggestions, please open an [Issue](https://github.com/shubh-jaiswal-897/DSA-Full-Code/issues) on GitHub.

---

**Last Updated:** June 2024  
**Version:** 2.0.0  
**Status:** Active Development & Maintenance
