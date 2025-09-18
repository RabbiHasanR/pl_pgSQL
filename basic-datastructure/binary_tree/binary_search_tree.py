class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class BinarySearchTree:
    
    def insert(self, root, val):
        if root is None:
            root = Node(val)
            return root
        
        if root.val > val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        
        return root
    
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.val, end=" ")
        self.inorder(root.right)
    
    def search(self, root, key):
        if root is None:
            return False
        
        if root.val == key:
            return True
        elif root.val > key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)
        
        

bst = BinarySearchTree()
values = [5,1,3,4,2,7]
root = None

for value in values:
    root = bst.insert(root, value)

print('root:', root.val)

print("Inorder:", end=" ")
bst.inorder(root)

print("find search:", bst.search(root, 0))