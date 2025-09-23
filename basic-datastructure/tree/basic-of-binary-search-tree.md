# Binary Search Tree (BST) – A Complete Guide

A **Binary Search Tree (BST)** is a special type of binary tree where:
- The **left subtree** of a node contains only nodes with values **less than** the node’s key.
- The **right subtree** of a node contains only nodes with values **greater than** the node’s key.
- Both the left and right subtrees are also BSTs.

## 🔑 Why BST?
- **Efficient searching**: O(log n) average time complexity.
- **Sorted traversal**: Inorder traversal yields elements in ascending order.
- **Basis for advanced structures**: AVL Trees, Red-Black Trees, B-Trees, etc.

## 🧩 Basic Terminologies
- **Root**: Topmost node.
- **Leaf**: Node with no children.
- **Height**: Longest path from root to leaf.
- **Inorder Successor**: The next larger node after a given node in inorder traversal.
- **Subtree**: Any node and its descendants.

## 🏗️ How to Build a BST
### Insert Operation (Pseudocode)
```plaintext
function insert(root, key):
    if root is NULL:
        return new Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else if key > root.data:
        root.right = insert(root.right, key)
    return root
```

### Example
Insert `[50, 30, 70, 20, 40, 60, 80]`:
```
        50
      /    \
    30      70
   /  \    /  \
 20   40  60  80
```

## 🔍 Searching in BST
### Pseudocode
```plaintext
function search(root, key):
    if root is NULL or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)
```

- **Search(40)**: Found.
- **Search(100)**: Not found.

## ❌ Deleting in BST
### Cases
1. **Node has no children (leaf)**: Delete directly.
2. **Node has one child**: Replace node with its child.
3. **Node has two children**: Replace with inorder successor (smallest in right subtree).

### Pseudocode
```plaintext
function delete(root, key):
    if root is NULL: return NULL
    if key < root.data:
        root.left = delete(root.left, key)
    else if key > root.data:
        root.right = delete(root.right, key)
    else:
        if root.left is NULL: return root.right
        if root.right is NULL: return root.left
        successor = minValue(root.right)
        root.data = successor.data
        root.right = delete(root.right, successor.data)
    return root
```

## 🌱 Inorder Successor
**Definition**: The node with the smallest key greater than the given node’s key.
- If node has a right subtree: Go to the leftmost node of the right subtree.
- If no right subtree: Go up until you come from a left child.

## 📊 Traversals in BST
- **Inorder**: Sorted order (e.g., `20 30 40 50 60 70 80`).
- **Preorder**: Root before children (e.g., `50 30 20 40 70 60 80`).
- **Postorder**: Root after children (e.g., `20 40 30 60 80 70 50`).
- **Level Order**: Breadth-first (e.g., `50 30 70 20 40 60 80`).

## 🎯 Print in Range [low, high]
Print all keys within the range `[L, R]`.

### Pseudocode
```plaintext
function printRange(root, L, R):
    if root is NULL: return
    if root.data > L:
        printRange(root.left, L, R)
    if L <= root.data <= R:
        print(root.data)
    if root.data < R:
        printRange(root.right, L, R)
```

### Example
Range `[30, 70]`: Output: `30 40 50 60 70`

## 🛤️ Print All Root-to-Leaf Paths
### Pseudocode
```plaintext
function printPaths(root, path):
    if root is NULL: return
    path.append(root.data)
    if root.left is NULL and root.right is NULL:
        print(path)
    else:
        printPaths(root.left, path)
        printPaths(root.right, path)
    path.pop()
```

### Example Paths
- `50 → 30 → 20`
- `50 → 30 → 40`
- `50 → 70 → 60`
- `50 → 70 → 80`

## 🧮 Other Key Operations
### Count Nodes
```plaintext
function count(root):
    if root is NULL: return 0
    return 1 + count(root.left) + count(root.right)
```

### Find Min & Max
```plaintext
function minValue(root):
    while root.left != NULL:
        root = root.left
    return root

function maxValue(root):
    while root.right != NULL:
        root = root.right
    return root
```

## ⏱️ Time Complexity
| Operation | Average   | Worst   |
|-----------|-----------|---------|
| Search    | O(log n)  | O(n)    |
| Insert    | O(log n)  | O(n)    |
| Delete    | O(log n)  | O(n)    |

**Note**: Worst case occurs if the tree becomes skewed (like a linked list). Balanced BSTs (e.g., AVL, Red-Black) mitigate this issue.




left subtree nodes < root
right subtree nodes > root
left & right subtrees are also bst


preorder(root,left,right)
inorder traversal of bst gives a increasing sorted sequence (left, root, right)
postorder(left,right,root)


search in bst time complexity is O(h)