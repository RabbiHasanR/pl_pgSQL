class MaxHeap:
    
    def __init__(self, data=None):
        self.heap_data = list(data)
    
    def build_heap_up_to_bottom(self):
        # heap = []
        # for num in self.heap_data:
        #     heap.append(num)
        #     i = len(heap) - 1
        #     while i > 0:
        #         parent = (i - 1) // 2
        #         if heap[parent] >= heap[i]:
        #             break
        #         heap[parent], heap[i] = heap[i], heap[parent]
                
        #         i = parent
        # self.heap_data = heap
        # return self.heap_data
                
        # without extra space      
        for j in range(len(self.heap_data)):
            i = j
            while i > 0:
                p = (i - 1) // 2
                if self.heap_data[p] >= self.heap_data[i]:
                    break
                self.heap_data[p], self.heap_data[i] = self.heap_data[i], self.heap_data[p]
                i = p
        
        return self.heap_data
    
    
    def heapify(self, i, n, data=None):
        if not data:
            data = self.heap_data
            
        while True:
            l = 2*i + 1
            r = 2*i + 2
            p = i
            if l < n and data[l] > data[p]:
                p = l
            if r < n and data[r] > data[p]:
                p = r
                
            if p == i:
                break
            data[p], data[i] = data[i], data[p]
            i = p
    
    def build_heap_using_heapify(self):
        n = len(self.heap_data)
        for i in range(n//2 - 1, -1, -1):
            self.heapify(i, n)
        
        return self.heap_data
    
    def heap_sort(self):
        max_heap = list(self.build_heap_using_heapify())
        
        for i in range(len(max_heap) - 1, 0, -1):
            max_heap[0], max_heap[i] = max_heap[i], max_heap[0]
            self.heapify(0, i, max_heap)
        return max_heap
    
    def peek_max_num(self):
        if not self.heap_data:
            raise IndexError("peek from empty heap")
        return self.heap_data[0]
    
    def pop(self):
        if not self.heap_data:
            raise IndexError("pop from empty heap")
        n = len(self.heap_data)
        self.heap_data[0], self.heap_data[n-1] = self.heap_data[n-1], self.heap_data[0]
        self.heapify(0, n-1)
        top = self.heap_data.pop()
        return top
    
    

class MinHeap:
    def __init__(self, data=None):
        self.min_heap = data
        
    def build_min_heap_up_to_bottom(self):
        for i in range(len(self.min_heap)):
            j = i
            while j > 0:
                p = (j - 1) // 2
                if self.min_heap[p] <= self.min_heap[j]:
                    break
                self.min_heap[p], self.min_heap[j] = self.min_heap[j], self.min_heap[p]
                j = p
        return self.min_heap
    
    def heapify(self, p, n, data=None):
        if not data:
            data = self.min_heap
        while True:
            l = 2 * p + 1
            r = 2 * p + 2
            smallest = p
            if l < n and data[l] < data[smallest]:
                smallest = l
            if r < n and data[r] < data[smallest]:
                smallest = r
            if smallest == p:
                break
            data[smallest], data[p] = data[p], data[smallest]
            p = smallest
    
    def build_min_heap_using_heapify(self):
        n = len(self.min_heap)
        
        for p in range(n//2 - 1, -1, -1):
            self.heapify(p, n)
        return self.min_heap
    
    def heap_short(self):
        min_heap = list(self.build_min_heap_using_heapify())
        n = len(min_heap)
        for end in range(n-1, 0, -1):
            min_heap[0], min_heap[end] = min_heap[end], min_heap[0]
            self.heapify(0, end, min_heap)
        return min_heap
    
    def peek(self):
        if not self.min_heap:
            raise IndexError("peek from empty heap")
        return self.min_heap[0]
    
    def pop(self):
        if not self.min_heap:
            raise IndexError("peek from empty heap")
        n = len(self.min_heap)
        self.min_heap[0], self.min_heap[n-1] = self.min_heap[n-1], self.min_heap[0]
        self.heapify(0, n-1)
        top = self.min_heap.pop()
        return top
    
nums = [10,20,15,30,40]
max_heap = MaxHeap(nums)

# print('build max heap up to bottom:', max_heap.build_heap_up_to_bottom())
print('build max heap using heapify:', max_heap.build_heap_using_heapify())
print('max heap sort:', max_heap.heap_sort())
print('peek max num:', max_heap.peek_max_num())
print('pop max num:', max_heap.pop())
print('after pop heap:', max_heap.heap_data)
print('pop max num:', max_heap.pop())
print('after pop heap:', max_heap.heap_data)


nums = [50,30,20,15,10,8,16]
min_heap = MinHeap(nums)
# print("build min heap from up to bottom:", min_heap.build_min_heap_up_to_bottom())
print('build min heap using heapify:', min_heap.build_min_heap_using_heapify())
# print("min heap sort:", min_heap.heap_short())
print("pirnt min num:", min_heap.peek())
print('pop:', min_heap.pop())
print("after pop heap:", min_heap.min_heap)
