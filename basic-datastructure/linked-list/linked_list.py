class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    
    def push_front(self, val):
        if not self.head:
            node = Node(val)
            self.head = node
            self.tail = self.head
        else:
            node = Node(val)
            node.next = self.head
            self.head = node
            
    def push_back(self, val):
        if not self.tail:
            node = Node(val)
            self.head = node
            self.tail = self.head
        else:
            temp = self.tail
            node = Node(val)
            temp.next = node
            self.tail = temp.next

    
    def pop_front(self):
        pass
    
    def pop_back(self):
        pass
    
    def print(self):
        temp = self.head
        
        while temp:
            print(temp.val, end="->")
            temp = temp.next
        print("null")


ll = LinkedList()

# build linked list
ll.push_front(1)
ll.push_front(2)
ll.push_back(3)
ll.push_front(4)

ll.print()
