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



some coding problems of binary tree:
build_tree

summ of all nodes

sum of all leafs

sum of kth level nodes

total nodes


subtree in binary tree