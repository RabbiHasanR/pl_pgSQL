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
        
    def delete(self, root, key):
        if root.val > key:
            root.left = self.delete(root.left, key)
        elif root.val < key:
            root.right = self.delete(root.right, key)
        
        else:
            # case 1
            if root.left is None and root.right is None:
                return None
            
            # case 2
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            # case 3
            IS = self.inorderSuccessor(root.right)
            root.val = IS.val
            root.right = self.delete(root.right, IS.val)
        
        return root
    
    def inorderSuccessor(self, root):
        while root.left:
            root = root.left
        return root
    
    def printInRange(self, root, x, y):
        if root is None:
            return
        
        if root.val >= x and root.val <= y:
            self.printInRange(root.left, x, y)
            print(root.val, end=" ")
            self.printInRange(root.right, x, y)
        
        elif root.val >= y:
            self.printInRange(root.left, x, y)
        else:
            self.printInRange(root.right, x, y)
            
    
    def printPath(self, path):
        for p in path:
            print(p, end="->")
        print("\n")
    
    def printRoot2Leaf(self, root, path):
        if root is None:
            return
        
        path.append(root.val)
        
        if root.left is None and root.right is None:
            self.printPath(path)
        else:
            self.printRoot2Leaf(root.left, path)
            self.printRoot2Leaf(root.right, path)
        
        path.pop()
        
        

bst = BinarySearchTree()
values = [5,1,3,4,2,7]
root = None

for value in values:
    root = bst.insert(root, value)

print('root:', root.val)

print("Inorder:", end=" ")
bst.inorder(root)
print("\nfind search:", end=" ")
print(bst.search(root, 0))

print("print in range:", end=" ")
bst.printInRange(root,2,8)

print("pirnt all paths root to leaf:")
path = []
bst.printRoot2Leaf(root, path)

print("delete node:", end=" ")
root = bst.delete(root, 3)

print("Inorder after delete:", end=" ")
bst.inorder(root)
