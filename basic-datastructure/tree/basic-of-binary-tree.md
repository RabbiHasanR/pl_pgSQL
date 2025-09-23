# Binary Tree: A Complete Guide

A **Binary Tree** is a fundamental data structure in computer science where each node has at most two children: a **left child** and a **right child**. It serves as the foundation for advanced structures like Binary Search Trees (BST), Heaps, and Syntax Trees.

## 🔑 Key Concepts

### 1. Basic Terminology
- **Root Node**: The topmost node of the tree.
- **Parent**: A node that has child nodes.
- **Children**: Nodes directly connected below a parent.
- **Sibling**: Nodes sharing the same parent.
- **Left Node / Right Node**: The two possible children of any parent node.
- **Leaf Node**: A node with no children.
- **Branches**: Paths connecting parent to child.
- **Levels**: Distance from the root (root is at level 0).
- **Height of Tree**: Longest path from root to a leaf.
- **Diameter of Tree**: The length of the longest path between any two nodes.
- **Subtree**: A tree formed by any node and its descendants.

### 2. Visualization
```
         (1) Root
        /   \
     (2)     (3)
    /   \       \
 (4)    (5)     (6)
               /
             (7)
```
- **Root**: 1
- **Parent of 2 and 3**: 1
- **Children of 2**: 4, 5
- **Siblings**: (2,3) and (4,5)
- **Leaf Nodes**: 4, 5, 7
- **Height**: 3
- **Levels**: 
  - Level 0: {1}
  - Level 1: {2,3}
  - Level 2: {4,5,6}
  - Level 3: {7}

## 🔄 Tree Traversal Methods
Traversal involves visiting each node in a tree exactly once. The following methods are commonly used:

1. **Preorder (Root → Left → Right)**  
   Example: `1 2 4 5 3 6 7`
2. **Inorder (Left → Root → Right)**  
   Example: `4 2 5 1 3 7 6`
3. **Postorder (Left → Right → Root)**  
   Example: `4 5 2 7 6 3 1`
4. **Level Order (Breadth First)**  
   Example: `1 2 3 4 5 6 7`


## 1. Complete Binary Tree

A binary tree is **complete** if:
- All levels, except possibly the last, are completely filled.
- In the last level, all nodes are as far left as possible (no gaps between nodes).

### Example (Complete but not full):
```
        1
      /   \
     2     3
    / \   /
   4   5 6
```
- The last level (nodes 4, 5, 6) is filled left to right with no gaps.
- This tree is complete but not full because node 3 has only one child.

## 2. Full Binary Tree (Proper/Strict Binary Tree)

A binary tree is **full** if:
- Every node has either **0 or 2 children** (no node has exactly one child).

### Example (Not Full):
```
        1
      /   \
     2     3
    / \     \
   4   5     6   ❌ (not full — node 3 has only one child)
```

### Example (Full):
```
        1
      /   \
     2     3
    / \   / \
   4   5 6   7   ✅ (full — every node has 0 or 2 children)
```

## 3. Perfect Binary Tree

A binary tree is **perfect** if:
- It is both **full** and **complete**.
- All internal nodes have **2 children**.
- All leaf nodes are at the **same depth/level**.

### Example:
```
        1
      /   \
     2     3
    / \   / \
   4   5 6   7
```
- Every level is fully filled.
- All nodes have either 0 or 2 children.
- All leaves (4, 5, 6, 7) are at the same level (level 2).
- This tree is **perfect** (and thus also full and complete).

## 4. Binary Search Tree (BST) Reminder

The terms **complete**, **full**, and **perfect** describe the **shape** of a binary tree. A **Binary Search Tree (BST)** adds an **ordering property**:
- For any node:
  - Values in the **left subtree** are **smaller** than the node’s value.
  - Values in the **right subtree** are **larger** than the node’s value.

### Combining BST with Tree Shapes
A BST can also have the properties of being complete, full, or perfect:
- **Complete BST**: Follows BST ordering and is complete (all levels filled except possibly the last, with nodes in the last level as far left as possible).
- **Full BST**: Follows BST ordering and is full (every node has 0 or 2 children).
- **Perfect BST**: Follows BST ordering and is perfect (both full and complete, with all leaves at the same level).

## ✅ Summary Table

| Term       | Condition                                                                 |
|------------|---------------------------------------------------------------------------|
| **Complete** | All levels filled except possibly the last, last level filled left-to-right. |
| **Full**     | Every node has 0 or 2 children (no node has exactly one child).            |
| **Perfect**  | Both full and complete, all leaves at the same level.                      |
| **BST**      | Ordering property: left subtree < root < right subtree.                    |



some coding problems of binary tree:
build_tree

summ of all nodes

sum of all leafs

sum of kth level nodes

total nodes


subtree in binary tree