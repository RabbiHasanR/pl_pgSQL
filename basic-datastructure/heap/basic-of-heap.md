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






# The Ultimate Guide to Heaps and Priority Queues

Heaps are a cornerstone of computer science, powering priority queues, scheduling systems, shortest path algorithms, and heapsort. This guide provides a comprehensive overview of heaps, their operations, complexities, and real-world applications.

## What Is a Heap?

A **heap** is a complete binary tree where each node satisfies the **heap property**:

- **Min Heap**: Every parent node is ≤ its children.
- **Max Heap**: Every parent node is ≥ its children.

Heaps are typically stored as arrays due to their complete binary tree structure.

### Indexing in a Heap (0-Based)

- **Left child**: `2*i + 1`
- **Right child**: `2*i + 2`
- **Parent**: `(i - 1)//2`

## Min Heap vs Max Heap

| Feature             | Min Heap                        | Max Heap                        |
|---------------------|---------------------------------|---------------------------------|
| **Parent vs Children** | Parent ≤ children              | Parent ≥ children              |
| **Root Value**      | Smallest element               | Largest element                |
| **Used for**        | Min-priority queues            | Max-priority queues            |

## Priority Queues and Heaps

A **priority queue** is a data structure where elements have priorities, and the highest (or lowest) priority element is served first.

- **Min Priority Queue**: Uses a Min Heap.
- **Max Priority Queue**: Uses a Max Heap.

Heaps enable efficient priority queue operations:
- **Insert**: O(log n)
- **Get/Remove Highest Priority**: O(log n)

Python’s `heapq` module implements a Min Heap priority queue.

## Heapify (Building a Heap)

**Heapify** transforms an array into a heap. There are two approaches:

### 1. Bottom-Up Heapify (Efficient)
- Start from the last non-leaf node and fix each subtree upward.
- **Time Complexity**: O(n)
- **Code Example**:

```python
def heapify_down(arr, i, n):  # Fix subtree rooted at i
    while True:
        l = 2*i + 1
        r = 2*i + 2
        smallest = i
        if l < n and arr[l] < arr[smallest]:
            smallest = l
        if r < n and arr[r] < arr[smallest]:
            smallest = r
        if smallest == i:
            break
        arr[i], arr[smallest] = arr[smallest], arr[i]
        i = smallest

def build_heap(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):  # Last non-leaf to root
        heapify_down(arr, i, n)
```

### 2. Top-Down Heapify (Repeated Insert)
- Insert elements one by one, fixing the heap each time.
- **Time Complexity**: O(n log n)
- **Code Example**:

```python
def insert_heap(arr, value):
    arr.append(value)
    i = len(arr) - 1
    while i > 0:  # Bubble up
        parent = (i-1)//2
        if arr[i] < arr[parent]:  # For min-heap
            arr[i], arr[parent] = arr[parent], arr[i]
            i = parent
        else:
            break
```

## Insert Operation (Bottom-Up)

1. Append the new element to the array.
2. "Bubble up" by swapping with the parent until the heap property is restored.

- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)

## Delete Operation (Root Removal)

1. Replace the root with the last element.
2. Remove the last element.
3. "Bubble down" (heapify down) from the root to restore the heap property.

- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)

## Heapsort

Heapsort leverages a heap to sort an array:

1. Build a max heap from the array: O(n)
2. Repeatedly extract the maximum and place it at the end: O(n log n)

- **Time Complexity**: O(n log n)
- **Space Complexity**: O(1) (in-place)
- **Code Example**:

```python
def heap_sort(arr):
    n = len(arr)
    # Build max heap
    for i in range(n//2 - 1, -1, -1):
        heapify_down_max(arr, i, n)

    # Extract max one by one
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_down_max(arr, 0, i)
```

**Note**: `heapify_down_max` is similar to `heapify_down` but ensures the parent is ≥ children for a max heap.

## Time & Space Complexities

| Operation                | Time Complexity | Space Complexity |
|--------------------------|-----------------|------------------|
| Build Heap (Bottom-Up)   | O(n)            | O(1)             |
| Build Heap (Top-Down)    | O(n log n)      | O(1)             |
| Insert                   | O(log n)        | O(1)             |
| Delete Root              | O(log n)        | O(1)             |
| Get Min / Max (Peek)     | O(1)            | O(1)             |
| Heapsort                 | O(n log n)      | O(1)             |

## Real-Life Use Cases

- **Priority Queues**: Task scheduling, CPU job scheduling.
- **Dijkstra’s Algorithm**: Shortest path in graphs.
- **A* Pathfinding**: Managing open sets of nodes.
- **Event Simulation**: Prioritizing the next event.
- **Median of Stream**: Using two heaps (min-heap + max-heap).
- **Bandwidth/Load Balancing**: Selecting the server with the lowest load.
- **Top-K Elements**: Tracking top K items with a heap of size K.

## Quick Python Demo with `heapq`

```python
import heapq

# Create min-heap
heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)

print(heap)  # [5, 10, 20]

# Pop smallest
print(heapq.heappop(heap))  # 5

# Build heap from list
arr = [40, 10, 30, 20, 50]
heapq.heapify(arr)
print(arr)  # [10, 20, 30, 40, 50]
```

## Conclusion

- Heaps are complete binary trees stored as arrays.
- Min heaps and max heaps differ by their heap property.
- Priority queues rely on heaps for efficient operations.
- Heapify builds a heap in O(n) (bottom-up).
- Insertion uses a bottom-up approach (bubble up).
- Deletion uses a top-down approach (bubble down).
- Heapsort sorts in-place with O(n log n) complexity.

Heaps are a versatile and efficient data structure, essential for many algorithms and real-world applications. 🚀