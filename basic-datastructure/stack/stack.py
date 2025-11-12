class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []
    
    def push(self, val):
        self.stack.append(val)
        if self.max_stack:
            self.max_stack.append(max(self.max_stack[-1], val))
        else:
            self.max_stack.append(val)
    
    def pop(self):
        self.max_stack.pop()
        return self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def peekMax(self):
        return self.max_stack[-1]
    
    def popMax(self):
        max_val = self.max_stack[-1]
        buffer = []
        
        while self.stack[-1] != max_val:
            buffer.append(self.stack.pop())
            self.max_stack.pop()
        
        self.stack.pop()
        self.max_stack.pop()
        
        while buffer:
            val = buffer.pop()
            self.stack.append(val)
            if self.max_stack:
                self.max_stack.append(max(self.max_stack[-1], val))
            else:
                self.max_stack.append(val)
        return max_val
    
    
maxstack = MaxStack()

maxstack.push(5)
maxstack.push(1)
maxstack.push(5)
print('top:', maxstack.top())
print('popmax:', maxstack.popMax())
print('top:', maxstack.top())
print('peekmax:', maxstack.peekMax())
print("pop:", maxstack.pop())

print(maxstack.stack)
print(maxstack.max_stack)