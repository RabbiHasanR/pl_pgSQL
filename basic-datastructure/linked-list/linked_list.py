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
        if self.head:
            val = self.head.val
            self.head = self.head.next
            return val
        return None
    
    def pop_back(self):
        # if tail node track
        # if self.head:
        #     if self.head == self.tail:
        #         val = self.head.val
        #         self.head = None
        #         self.tail = None
        #         return val
            
        #     temp = self.head
        #     while temp.next != self.tail:
        #         temp = temp.next
        #     val = self.tail.val
        #     temp.next = None
        #     self.tail = temp
        #     return val
        # return None
        
        
        # if tail node not track
        if not self.head:
            return None
        if not self.head.next:
            val = self.head.val
            self.head = None
            return val
        
        prev = self.head
        curr = self.head.next
        
        while curr.next:
            prev = curr
            curr = curr.next
        
        val = curr.val
        prev.next = None
        return val
    
    
    def insert(self, val, pos):
        if pos < 0:
            return
        if pos-1 == 0:
            self.push_front(val)
        else:
            node = Node(val)
            i = 0
            temp = self.head
            while i < pos - 1 and temp.next:
                temp = temp.next
                i += 1
            
            node.next = temp.next
            temp.next = node
            
            
    def search(self, val):
        if not self.head:
            return False
        
        temp = self.head
        
        while temp:
            if temp.val == val:
                return True
            temp = temp.next
        
        return False
        
            
    
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

print("pop front:", ll.pop_front())
ll.print()
print("pop back:", ll.pop_back())
ll.print()
print("pop back:", ll.pop_back())
ll.print()
print("pop back:", ll.pop_back())
ll.print()

ll.insert(1,1)
ll.print()
ll.insert(2,3)
ll.print()
ll.insert(3,2)
ll.print()
print('found:', ll.search(4))