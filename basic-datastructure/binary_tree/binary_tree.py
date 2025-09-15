from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class BinaryTree:
    def __init__(self):
        self.idx = -1
        
    def build_tree(self, nodes):
        self.idx +=1
        
        if nodes[self.idx] == -1:
            return None
        
        newNode = Node(nodes[self.idx])
        newNode.left = self.build_tree(nodes)
        newNode.right = self.build_tree(nodes)
        
        return newNode

    def pre_oder(self, root):
        if root is None:
            return
        print(root.val, end=" ")
        self.pre_oder(root.left)
        self.pre_oder(root.right)
    
    def in_order(self, root):
        if root is None:
            return
        
        self.in_order(root.left)
        print(root.val, end=" ")
        self.in_order(root.right)
    
    def post_order(self, root):
        if root is None:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.val, end=" ")
        
    def level_order(self, root):
        q = deque()
        q.append(root)
        q.append(None)
        
        while q:
            currentNode = q.popleft()
            if currentNode is None:
                print("\n")
                if not q:
                    break
                else:
                    q.append(None)
            else:
                print(currentNode.val, end=" ")
                if currentNode.left:
                    q.append(currentNode.left)
                if currentNode.right:
                    q.append(currentNode.right)
        
nodes = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]

binary_tree = BinaryTree()

root = binary_tree.build_tree(nodes)
print(root.val)

binary_tree.pre_oder(root)
print("\n")
binary_tree.in_order(root)
print("\n")
binary_tree.post_order(root)
print("\n")
binary_tree.level_order(root)