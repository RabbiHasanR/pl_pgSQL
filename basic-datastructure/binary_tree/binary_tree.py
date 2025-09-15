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
                    
    def height(self, root):
        if root is None:
            return 0
        
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        
        return max(left_height, right_height) + 1
    
    # this time complexity is O(n^2)
    def diameter(self, root):
        if root is None:
            return 0
        left_diameter = self.diameter(root.left)
        right_diameter = self.diameter(root.right)
        root_diameter = self.height(root.left) + self.height(root.right) + 1
        
        return max(left_diameter, right_diameter, root_diameter)
    
    # this time complexity is O(n)
    def optimize_diameter(self,root):
        if root is None:
            return {"height":0, "diameter": 0}
        left_h_d = self.optimize_diameter(root.left)
        right_h_d = self.optimize_diameter(root.right)
        
        height = max(left_h_d["height"], right_h_d["height"]) + 1
        root_d = left_h_d["height"] + right_h_d["height"] + 1
        
        return {"height": height, "diameter": max(root_d, left_h_d["diameter"], right_h_d["diameter"])}
        
    def sum_of_all_nodes(self, root):
        if root is None:
            return 0
        left_sum = self.sum_of_all_nodes(root.left)
        right_sum = self.sum_of_all_nodes(root.right)
        return root.val + left_sum + right_sum
    
    def total_nodes(self, root):
        if root is None:
            return 0
        
        left_total = self.total_nodes(root.left)
        right_total = self.total_nodes(root.right)
        return 1 + left_total + right_total
    
nodes = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]

binary_tree = BinaryTree()

root = binary_tree.build_tree(nodes)
print(root.val)
print("pre order:")
binary_tree.pre_oder(root)
print("\nin order:\n")
binary_tree.in_order(root)
print("\npost order:\n")
binary_tree.post_order(root)
print("\nlevel order:\n")
binary_tree.level_order(root)

print("height:", binary_tree.height(root))
print("diameter:", binary_tree.diameter(root))
print("optimize diameter:", binary_tree.optimize_diameter(root))
print("sum of all nodes:", binary_tree.sum_of_all_nodes(root))
print("total nodes:", binary_tree.total_nodes(root))