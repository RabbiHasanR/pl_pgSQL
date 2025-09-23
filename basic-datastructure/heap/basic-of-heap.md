# Array Representation of a Binary Tree

The **array representation** of a binary tree stores the tree's nodes in an array (or list) instead of using pointers (e.g., left and right child references). This approach is particularly efficient for **complete** or **perfect binary trees** and is commonly used in data structures like **heaps**.

## Index Rules (0-Based Indexing)

For a node at index `i`:
- **Root**: Stored at index `0`.
- **Left Child**: Located at index `2*i + 1`.
- **Right Child**: Located at index `2*i + 2`.
- **Parent**: Located at index `(i - 1) // 2`.

### Alternative: 1-Based Indexing (Common in Textbooks for Heaps)
For a node at index `i`:
- **Root**: Stored at index `1`.
- **Left Child**: Located at index `2*i`.
- **Right Child**: Located at index `2*i + 1`.
- **Parent**: Located at index `i // 2`.

**Note**: This guide uses **0-based indexing** for examples unless specified otherwise.

## Example 1: Perfect Binary Tree

### Tree
```
        1
      /   \
     2     3
    / \   / \
   4   5 6   7
```

### Array (0-Based)
```
[1, 2, 3, 4, 5, 6, 7]
```

### Verification
- `arr[0] = 1` (root) → Children: `arr[1] = 2`, `arr[2] = 3`
- `arr[1] = 2` → Children: `arr[3] = 4`, `arr[4] = 5`
- `arr[2] = 3` → Children: `arr[5] = 6`, `arr[6] = 7`

✅ The array correctly represents the perfect binary tree.

## Example 2: Complete Binary Tree

### Tree
```
        1
      /   \
     2     3
    / \   /
   4   5 6
```

### Array (0-Based)
```
[1, 2, 3, 4, 5, 6]
```

### Verification
- `arr[0] = 1` → Children: `arr[1] = 2`, `arr[2] = 3`
- `arr[1] = 2` → Children: `arr[3] = 4`, `arr[4] = 5`
- `arr[2] = 3` → Left child: `arr[5] = 6`, Right child: index `6` doesn’t exist (OK, as it’s a complete tree).

✅ The array correctly represents the complete binary tree.

## Example 3: Incomplete Binary Tree (Not Complete)

### Tree
```
        1
      /   \
     2     3
          /
         6
```

### Array (0-Based)
```
[1, 2, 3, None, None, 6]
```

### Verification
- `arr[0] = 1` → Children: `arr[1] = 2`, `arr[2] = 3`
- `arr[1] = 2` → Children: `arr[3] = None`, `arr[4] = None` (no children)
- `arr[2] = 3` → Left child: `arr[5] = 6`, Right child: index `6` is `None`

**Note**: For incomplete binary trees, the array may contain `None` values to represent missing nodes, which can waste space.

## Key Uses

- **Heap Data Structure**: Array representation is ideal for **max-heaps** and **min-heaps** because they are complete binary trees.
- **Efficient Navigation**: Parent and child nodes can be accessed using simple index calculations.
- **Space Efficiency**: For complete or perfect binary trees, no space is wasted, unlike pointer-based representations.

## ✅ Summary

- **Storage**: Nodes are stored level by level in an array.
- **Index Formulas (0-Based)**:
  - Left child: `2*i + 1`
  - Right child: `2*i + 2`
  - Parent: `(i - 1) // 2`
- **Best Use Case**: Complete or perfect binary trees, as they avoid gaps (`None` values) in the array.
- **Limitations**: For arbitrary or incomplete binary trees, the array may include `None` values, reducing space efficiency.









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






max heap

min heap

insert in max heap
delete in max heap
heap short
heapify
priority queues