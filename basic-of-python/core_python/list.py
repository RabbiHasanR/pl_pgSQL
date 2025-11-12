import sys
empty_list = []
print(sys.getsizeof(empty_list))

for i in range(10):
    empty_list.append(i)
    print(f"Length: {len(empty_list)}, Size: {sys.getsizeof(empty_list)} bytes")
    print(f"  Appended value: {i}")
    print(f"  Address of i: {hex(id(i))}")
    print("-" * 40)
    
    

    

# A list of integers
numbers = [1,2,3,4]
print(f"Size: {sys.getsizeof(numbers)} bytes")
numbers.append(4)
print(f"Size: {sys.getsizeof(numbers)} bytes")
print("numbers:", numbers)
# A list with mixed data types
mixed_list = [1, "hello", 3.14, True, [10, 20]]
print('mixed_list:', mixed_list)


# Accessing Items (Indexing)

fruits = ["apple", "banana", "cherry", "date"]

# Get the first item (index 0)
print(fruits[0])  
# Output: 'apple'

# Get the third item (index 2)
print(fruits[2])  
# Output: 'cherry'

# Use negative indexing to count from the end
# -1 is the last item
print(fruits[-1]) 
# Output: 'date'

# -2 is the second-to-last item
print(fruits[-2]) 
# Output: 'cherry'

# Slicing (Getting Sub-lists)
# we can slice a list to get a new list with a subset of items. the syntax is my_list[start:stop:step]
# start: The index to begin (inclusive).

# stop: The index to stop (exclusive - it does not include this item).

# step: The gap between items (default is 1).

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get items from index 2 up to (but not including) index 5
print(numbers[2:5])   
# Output: [2, 3, 4]

# Get items from the beginning up to index 4
print(numbers[:4])    
# Output: [0, 1, 2, 3]

# Get items from index 6 to the end
print(numbers[6:])    
# Output: [6, 7, 8, 9]

# Get every second item
print(numbers[::2])   
# Output: [0, 2, 4, 6, 8]

# Get a copy of the entire list
print(numbers[:])     
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Reverse the list with a slice
print(numbers[::-1])  
# Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(numbers[::-2])

print(numbers[-1:-6:-1])

print(numbers[1:-6])

# Common List Methods and Operations

pets = ["cat", "dog"]

# --- ADDING ---

# Add one item to the end
# time 0(1) and space 0(1)
pets.append("bird")
print(pets)  # Output: ['cat', 'dog', 'bird']

# Add an item at a specific index
# time 0(n) and space 0(1)
pets.insert(1, "lizard")  
print(pets)  # Output: ['cat', 'lizard', 'dog', 'bird']

# Add all items from another list to the end
# time 0(n) and space 0(k)
more_pets = ["hamster", "fish"]
pets.extend(more_pets)
print(pets)  # Output: ['cat', 'lizard', 'dog', 'bird', 'hamster', 'fish']

# --- REMOVING ---

# Remove the first item that matches a value
# time 0(n) and space 0(1)
pets.remove("lizard")
print(pets)  # Output: ['cat', 'dog', 'bird', 'hamster', 'fish']

# Remove an item by its index and get its value
# (default: removes the last item)
# time 0(1) and space 0(1)
last_pet = pets.pop()
print(last_pet) # Output: 'fish'
print(pets)     # Output: ['cat', 'dog', 'bird', 'hamster']

# Remove item at index 1
# time 0(n-i) and space 0(1)
removed_pet = pets.pop(1)
print(removed_pet) # Output: 'dog'
print(pets)        # Output: ['cat', 'bird', 'hamster']

# Remove an item by index using the 'del' keyword
# time 0(n-i) and space 0(1)
del pets[0]
print(pets)  # Output: ['bird', 'hamster']

# Sorting and Reversing

numbers = [5, 1, 10, 3]
names = ["Zach", "Alice", "Bob"]

# --- IN-PLACE (Modifies the original list) ---
# python built in sort method use Timsort algorithm
# Sort the list in-place
# time 0(nlogn) and space 0(1)
numbers.sort()
print(numbers)  # Output: [1, 3, 5, 10]

# Sort in-place in reverse
# time 0(nlogn) and space 0(1)
names.sort(reverse=True)
print(names)    # Output: ['Zach', 'Bob', 'Alice']

# Reverse the list in-place
# time 0(n) and space 0(1)
numbers.reverse()
print(numbers)  # Output: [10, 5, 3, 1]

# --- CREATING A NEW LIST ---

# Use the 'sorted()' function to return a new sorted list
# (The original is unchanged)
numbers = [5, 1, 10, 3]
# time 0(nlogn) and space 0(n)
new_sorted_list = sorted(numbers)
print(new_sorted_list)  # Output: [1, 3, 5, 10]
print(numbers)          # Output: [5, 1, 10, 3]

# Other Useful Functions and Keywords

numbers = [1, 2, 2, 3, 4]

# Get the length of a list
# time 0(1) and space 0(1)
print(len(numbers))  
# Output: 5

# Check if an item is in the list
# time 0(n) and space 0(1)
print(2 in numbers)  
# Output: True
# time 0(n) and space 0(1)
print(99 in numbers) 
# Output: False

# Find the index of the first matching item
# time 0(n) and space 0(1)
print(numbers.index(2)) 
# Output: 1

# Count how many times an item appears
# time 0(n) and space 0(1)
print(numbers.count(2)) 
# Output: 2

# Loop over a list
# time 0(n) and space 0(1)
for num in numbers:
    print(num)
# Output:
# 1
# 2
# 2
# 3
# 4