class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        



class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    
    def push_front(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            new_node.next = temp
            temp.prev = new_node
            self.head = new_node
            
    def push_back(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        
        else:
            temp = self.tail
            temp.next = new_node
            new_node.prev = temp
            self.tail = new_node
            
    def pop_front(self):
        if not self.head:
            return None
        val = self.head.val
        temp = self.head.next
        if temp:
            temp.prev = None
        self.head = temp
        return val
    
    def pop_back(self):
        if not self.head:
            return None
        val = self.tail.val
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            temp = self.tail.prev
            temp.next = None
            self.tail = temp
        return val
    
    def print_front_to_back(self):
        temp = self.head
        while temp:
            print(temp.val, end="->")
            temp = temp.next
        print(None)
    
    def print_back_to_print(self):
        temp = self.tail
        
        while temp:
            print(temp.val, end="->")
            temp = temp.prev
        print(None)
    
    

dll = DoublyLinkedList()


# build linked list
dll.push_front(1)
dll.push_front(2)
dll.push_back(3)
dll.push_front(4)

dll.print_front_to_back()
dll.print_back_to_print()
print(dll.pop_back())
dll.print_front_to_back()
print(dll.pop_back())
dll.print_front_to_back()
print(dll.pop_back())
dll.print_front_to_back()
print(dll.pop_back())
dll.print_front_to_back()
print(dll.pop_back())
dll.print_front_to_back()
