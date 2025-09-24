class MaxHeap:
    
    def build_heap_up_to_bottom(self, data):
        # heap = []
        # for num in data:
        #     heap.append(num)
        #     i = len(heap) - 1
        #     while i > 0:
        #         parent = (i - 1) // 2
        #         if heap[parent] >= heap[i]:
        #             break
        #         heap[parent], heap[i] = heap[i], heap[parent]
                
        #         i = parent
        # return heap
                
        # without extra space      
        for j in range(len(data)):
            i = j
            while i > 0:
                p = (i - 1) // 2
                if data[p] >= data[i]:
                    break
                data[p], data[i] = data[i], data[p]
                i = p
        
        return data
    
    
    def heapify(self, data, i, n):
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
    
    def build_heap_using_heapify(self, data):
        n = len(data)
        for i in range(n//2 - 1, -1, -1):
            self.heapify(data, i, n)
        
        return data
    
    def heap_sort(self, data):
        max_heap = self.build_heap_using_heapify(data)
        
        for i in range(len(max_heap) - 1, 0, -1):
            max_heap[0], max_heap[i] = max_heap[i], max_heap[0]
            self.heapify(max_heap, 0, i)
        return max_heap

nums = [10,20,15,30,40]
max_heap = MaxHeap()

print('build max heap up to bottom:', max_heap.build_heap_up_to_bottom(nums))
print('build max heap using heapify:', max_heap.build_heap_using_heapify(nums))
print('max heap sort:', max_heap.heap_sort(nums))