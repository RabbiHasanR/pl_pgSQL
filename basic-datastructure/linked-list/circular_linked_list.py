class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    
    def insertAtHead(self, val):
        new_node = Node(val)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
            
    def insertAtTail(self, val):
        new_node = Node(val)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
            
            
    def deleteAtHead(self):
        if not self.head:
            return
        elif self.head == self.tail:
            val = self.head.val
            self.head = None
            self.tail = None
            return val
        else:
            temp = self.head
            self.head = self.head.next
            self.tail.next = self.head
            return temp.val
        
    
    def deleteAtTail(self):
        if not self.head:
            return
        elif self.head == self.tail:
            val = self.head.val
            self.head = None
            self.tail = None
            return val
        else:
            temp = self.tail
            prev = self.head
            while prev.next != self.tail:
                prev = prev.next
            
            prev.next = self.head
            self.tail = prev
            return temp.val
        
    def print(self):
        if not self.head:
            return
        print(self.head.val, end="->")
        temp = self.head.next
        while temp != self.head:
            print(temp.val, end="->")
            temp = temp.next

        print(temp.val)


cll = CircularLinkedList()
cll.insertAtHead(1)
cll.insertAtHead(2)
cll.insertAtHead(3)
cll.print()
cll.insertAtTail(4)
cll.insertAtTail(5)
cll.print()
# print('d:',cll.deleteAtHead())
# cll.print()
# print('d',cll.deleteAtHead())
# cll.print()
# print('d:',cll.deleteAtHead())
# cll.print()
# print('d:',cll.deleteAtHead())
# cll.print()
# print('d:',cll.deleteAtHead())
# cll.print()
print('dt:', cll.deleteAtTail())
cll.print()
print('dt:', cll.deleteAtTail())
cll.print()
print('dt:', cll.deleteAtTail())
cll.print()
print('dt:', cll.deleteAtTail())
cll.print()
print('dt:', cll.deleteAtTail())
cll.print()