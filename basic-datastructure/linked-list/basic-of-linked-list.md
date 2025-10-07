# 🧩 Linked List Explained — From Basics to Advanced

When you start learning data structures, one of the most fundamental topics you’ll encounter after arrays is the **Linked List**.

But what exactly is a **Linked List**?  
And how is it different from arrays?

Let’s explore step-by-step.

## 🔹 What is a Linked List?

A **Linked List** is a linear data structure — just like an array — where data elements are arranged one after another.

But there’s one key difference:

👉 In an array, elements are stored in contiguous memory locations.  
👉 In a linked list, elements (called **nodes**) can be stored anywhere in memory, and each node stores a **reference (or link)** to the next node.

## 🧠 What is Contiguous Memory?

**Contiguous memory** means all elements of an array are stored side by side in consecutive memory addresses.

For example, suppose you have an integer array:

```c
int arr[4] = {10, 20, 30, 40};
```

If the first element `arr[0]` is at memory address 1000, then:

| Element | Value | Address |
|---------|-------|---------|
| arr[0]  | 10    | 1000    |
| arr[1]  | 20    | 1004    |
| arr[2]  | 30    | 1008    |
| arr[3]  | 40    | 1012    |

*(Each `int` takes 4 bytes.)*

That’s why arrays are fast to access by index (**O(1)** time), because we can directly compute the address of `arr[i]` using:

```
Address = BaseAddress + (i × size_of_data_type)
```

But arrays have limitations:  
- Their size is fixed at creation time.  
- Insertion and deletion are costly (**O(n)**), since we may need to shift elements.

## 🔹 Why Linked List?

Unlike arrays, linked lists use **non-contiguous memory**.

Each element (called a **node**) stores:  
- **Data**  
- A **pointer (reference)** to the next node  

So nodes can be scattered in memory — they’re “linked” together via pointers.

**Example structure** (in C-style pseudo code):

```c
struct Node {
    int data;
    Node* next;
};
```

**Visual representation**:

```
[10 | *] --> [20 | *] --> [30 | *] --> NULL
```

- 10, 20, 30 are data  
- `*` is a pointer to the next node  
- `NULL` means the end of the list  

## 🧩 Types of Linked Lists

There are three main types of linked lists:

### 1️⃣ Singly Linked List

Each node stores:  
- `data`  
- `next` pointer (address of next node)  

**Example**:

```
Head → [10 | *] → [20 | *] → [30 | NULL]
```

**Insertion Example (Python)**:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example:
ll = SinglyLinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()
```

**Output**:

```
10 -> 20 -> 30 -> None
```

### 2️⃣ Doubly Linked List

Each node has two pointers:  
- `prev` → points to the previous node  
- `next` → points to the next node  

So you can traverse in both directions.

**Example**:

```
NULL ← [10 | * | *] ↔ [20 | * | *] ↔ [30 | * | NULL]
```

**Python Example**:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

# Example:
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.display_forward()
```

**Output**:

```
10 <-> 20 <-> 30 <-> None
```

### 3️⃣ Circular Linked List

In a circular linked list, the last node points back to the first node, forming a circle.

**Singly Circular Linked List**:

```
[10 | *] → [20 | *] → [30 | *] ↺
```

**Doubly Circular Linked List**:

```
↺ [10] ⇄ [20] ⇄ [30] ⇄ [10] ↺
```

Circular lists are often used in:  
- Round-robin scheduling  
- Media playlists  
- Circular buffers  

## 🔹 Dynamic Memory Advantage

Unlike arrays, linked lists can grow or shrink **dynamically** during runtime.

You don’t need to pre-define the size — you just allocate a new node when needed.

### ✅ Adding a node
- Create a new node using `new` or `malloc` (or dynamically in Python)  
- Link it by updating pointers  
- No need to move existing data  

### ✅ Removing a node
- Adjust the previous node’s pointer to skip the deleted node  
- Free memory (in C/C++) or let Python’s garbage collector handle it  

**Example (Deleting node by value)**:

```python
def delete(self, key):
    temp = self.head
    if temp and temp.data == key:
        self.head = temp.next
        return
    prev = None
    while temp and temp.data != key:
        prev = temp
        temp = temp.next
    if temp:
        prev.next = temp.next
```

## ⚙️ Linked List vs Array — Summary

| Feature              | Array                  | Linked List                  |
|----------------------|------------------------|------------------------------|
| **Memory**           | Contiguous             | Non-contiguous               |
| **Size**             | Fixed                  | Dynamic                      |
| **Access time**      | O(1) (direct index)    | O(n) (traverse nodes)        |
| **Insertion/Deletion** | Costly (need shifting) | Easy (just change pointers)  |
| **Extra memory**     | No                     | Yes (needs pointer storage)  |

## 💡 When to Use a Linked List?

**Use linked lists when**:  
- You need frequent insertion and deletion  
- You don’t know the number of elements in advance  
- You want to avoid shifting elements (like in arrays)  

**Avoid linked lists when**:  
- You need random access (like `arr[5]`)  
- Memory overhead (due to pointers) is a concern  

## 🧾 Final Thoughts

A **Linked List** is one of the most flexible and dynamic data structures — it teaches you how memory and pointers truly work under the hood.

It’s the foundation of more advanced structures like:  
- Stacks  
- Queues  
- Hash tables  
- Graphs  

Understanding it deeply will help you become a stronger programmer and problem-solver.