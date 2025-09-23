from collections import deque, defaultdict

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
        


class NTree:
    def build_tree(self, root, parent, val):
        if root is None:
            root = Node(parent)
            root.children.append(Node(val))
            return root
        
        def dfs(node):
            if node.val == parent:
                node.children.append(Node(val))
                return True
            for ch in node.children:
                if dfs(ch):
                   return True
            return False
        
        inserted = dfs(root)
        if not inserted:
            new_parent = Node(parent)
            new_parent.children.append(Node(val))
            root.children.append(new_parent)
        return root 
    
    def preeorder(self, root):
        res = []
        def dfs(node):
            if not node:
                return
            res.append(node.val)
            for ch in node.children:
                dfs(ch)
        dfs(root)
        return res
    
    def postorder(self, root):
        res = []
        def dfs(node):
            if not node:
                return
            for ch in node.children:
                dfs(ch)
            res.append(node.val)
        dfs(root)
        return res
    
    def levelorder(self, root):
        if not root:
            return []
        q = deque()
        q.append([root, 1])
        res = defaultdict(list)
        while q:
            item = q.popleft()
            node, level = item[0], item[1]
            res[level].append(node.val)
            for ch in node.children:
                q.append([ch, level + 1])
        
        return res.values()
    
    def search(self, root, key):
        if not root:
            return False
        if root.val == key:
            return True
        for ch in root.children:
            find = self.search(ch, key)
            if find:
                return True
        return False
            
    def height(self, root):
        if not root:
            return 0
        if not root.children:
            return 1
        return 1 + max(self.height(ch) for ch in root.children)
    
edges = [
    (1,2), (1,3), (1,4),
    (3,5), (3,6),
    (4,7)
]

tree = NTree()
root = None
for p, c in edges:
    root = tree.build_tree(root, p, c)
    

print("preorder:", tree.preeorder(root))
print("postorder:", tree.postorder(root))
print("levelorder:", tree.levelorder(root))
print("search:", tree.search(root, 10))
print("height:", tree.height(root))