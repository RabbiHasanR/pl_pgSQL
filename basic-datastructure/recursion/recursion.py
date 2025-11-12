# print 1 to n
def print_nums(n):
    if n == 0:
        return
    print(n)
    print_nums(n-1)

print_nums(4)


# print N Factorial

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print("factorial:",factorial(5))

# sum of n nums

def sum(n):
    if n == 0:
        return 0
    return n + sum(n - 1)

print("sum of n num:", sum(5))


# fibonacci

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

print("fib:", fib(6))


# fibonacci using recursion + memoization
memo = {}

def fib_memo(n):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        result = n
    else:
        result = fib_memo(n-1) + fib_memo(n-2)
    
    memo[n] = result
    return result
    
print("fib:", fib_memo(6))



# fibonacci using memorization.  also can generate fibonacci sequence

def memo_fib(n):
    memo = {}
    
    # if n == 0:
    #     return 0
    
    for i in range(0, n + 1):
        if i == 0:
            result = 0
        elif i <= 2:
            result = 1
        
        else:
            result = memo[i - 1] + memo[i - 2]
        
        memo[i] = result
    
    # return memo[n]
    return memo.values()

print("fib:", memo_fib(6))




# check is array sorted

def is_sorted(nums, n):
    if n == 0 or n == 1:
        return True
    return nums[n - 1] >= nums[n - 2] and is_sorted(nums, n - 1)


nums  = [1,2,3,8,5,6]
print("is sorted:", is_sorted(nums, 6))


# recursive binary search

def binary_search(nums, tar, start, end):
    if start <= end:
        mid = (start + end) // 2
        if nums[mid] == tar:
            return mid
        elif nums[mid] >= tar:
            return binary_search(nums, tar, start, mid - 1)
        else:
            return binary_search(nums, tar, mid + 1, end)
    return -1


nums = [-1,0,3,5,9,12]
tar = 50

print('binary search:', binary_search(nums, tar, 0, len(nums) - 1))

# print all subsets

def print_all_subsets(nums, ans, i):
    if i == len(nums):
        print(ans)
        return
    ans.append(nums[i])
    print_all_subsets(nums, ans, i + 1)
    ans.pop()
    print_all_subsets(nums, ans, i + 1)

print("print all subsets:")
nums = [1,2,3]
print_all_subsets(nums, [], 0)


def print_all_subsets_without_duplicate(nums, ans, i):
    if i == len(nums):
        print(ans)
        return
    ans.append(nums[i])
    print_all_subsets_without_duplicate(nums, ans, i + 1)
    ans.pop()
    idx = i + 1
    
    while idx < len(nums) and nums[i] == nums[idx]:
        idx += 1
    
    print_all_subsets_without_duplicate(nums, ans, idx)
    
print("print all subsets without duplicates:")
nums = [1,2,2]
nums.sort()
print_all_subsets_without_duplicate(nums, [], 0)


# permutations 


def permutations(nums, i, res):
    if i == len(nums):
        res.append(nums[:])
        return
    for j in range(i, len(nums)):
        nums[i], nums[j] = nums[j], nums[i]
        permutations(nums, i + 1, res)
        nums[i], nums[j] = nums[j], nums[i]
    
    return res

nums=[1,2,3]

print("all permutations:", permutations(nums, 0, []))


# N queens

def is_safe(board, row, col, n):
    # horizontal
    for i in range(n):
        if board[row][i] == 'Q':
            return False
    
    # vertical 
    for i in range(n):
        if board[i][col] == 'Q':
            return False
    
    # left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    
    # right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    return True

def nQueens(board, row, n, res):
    if row == n:
        res.append(["".join(row) for row in board])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            nQueens(board, row + 1, n, res)
            board[row][col] = '.'
    
    
n = 4
board = [["."] * n for _ in range(n)]
res = []
nQueens(board, 0, n, res)

print("nQueens:", res)


# Sudoku Solver. sudoku borad is 9 * 9 matrix

def isSafeDigit(board, row, col, digit):
    # horizontal
    for i in range(9):
        if board[row][i] == digit:
            return False
    
    # vertical
    for i in range(9):
        if board[i][col] == digit:
            return False
    
    # 3x3 grid check
    # if row <= 2 and row >= 0:
    #     start_row = 0
    # if row <= 5 and row >= 3:
    #     start_row = 3
    # if row <= 8 and row >= 6:
    #     start_row = 6
        
    # if col <= 2 and col >= 0:
    #     start_col = 0
    # if col <= 5 and col >= 3:
    #     start_col = 3
    # if col <= 8 and col >= 6:
    #     start_col = 6
        
    start_row = (row//3) * 3
    start_col = (col//3) * 3
    
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == digit:
                return False
    return True


def sudoku_solver(board, row, col):
    if row == 9:
        return True
    
    nextRow = row
    nextCol = col + 1
    if nextCol == 9:
        nextRow += 1
        nextCol = 0
        
    if board[row][col] !='.':
        return sudoku_solver(board, nextRow, nextCol)
    
    for digit in range(1, 10):
        if isSafeDigit(board, row, col, str(digit)):
            board[row][col] = str(digit)
            if sudoku_solver(board, nextRow, nextCol):
                return True
            board[row][col] = '.'
    return False


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print('soduku solver:', sudoku_solver(board,0,0))
print(board)



# rat in a maze

# def get_paths(mat, n, row, col, vis, ans, path):
#     if row < 0 or col < 0 or row >= n or col >= n or mat[row][col] == 0 or vis[row][col]:
#         return
    
#     if row == n - 1 and col == n - 1:
#         ans.append(path)
#         return
    
#     vis[row][col] = True
#     # down
#     get_paths(mat, n, row + 1, col, vis, ans, path+"D")
#     # up
#     get_paths(mat, n, row - 1, col, vis, ans, path+"U")
#     # left
#     get_paths(mat, n, row, col - 1, vis, ans, path+"L")
#     # right
#     get_paths(mat, n, row, col + 1, vis, ans, path+"R")
    
#     vis[row][col] = False


# without using visited 
def get_paths(mat, n, row, col, ans, path):
    if row < 0 or col < 0 or row >= n or col >= n or mat[row][col] == 0:
        return
    
    if row == n - 1 and col == n - 1:
        ans.append(path)
        return
    
    mat[row][col] = 0
    # down
    get_paths(mat, n, row + 1, col, ans, path+"D")
    # up
    get_paths(mat, n, row - 1, col,  ans, path+"U")
    # left
    get_paths(mat, n, row, col - 1,  ans, path+"L")
    # right
    get_paths(mat, n, row, col + 1,  ans, path+"R")
    
    mat[row][col] = 1
    
    
mat =  [[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
n = len(mat)    
# visited = [[False] * n for _ in range(n)]
ans = []

# get_paths(mat, n, 0, 0, visited, ans, "")
get_paths(mat, n, 0, 0, ans, "")


print("get all paths:",ans)



# combination sum
import json
def comb_sum(nums, i, comb, ans, tar):
    if i == len(nums) or tar < 0:
        return
    
    if tar == 0:
        ans.add(str(comb[:]))
        return
    
    comb.append(nums[i])
    comb_sum(nums, i + 1, comb, ans, tar - nums[i]) # single inclusion
    comb_sum(nums, i, comb, ans, tar - nums[i]) # multi inclusion
    comb.pop()
    comb_sum(nums, i + 1, comb, ans, tar)
    
nums = [2,3,5]
ans = set()
target = 8

comb_sum(nums, 0, [], ans, target)

print([json.loads(item) for item in ans])


# Palindrome Partitioning

def isPalindrome(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def get_all_partion(s, partions, ans):
    if len(s) == 0:
        ans.append(partions[:])
        return
    for i in range(len(s)):
        part = s[0:i+1]
        if isPalindrome(part):
            partions.append(part)
            get_all_partion(s[i+1:], partions, ans)
            partions.pop()
            

# s = 'aab'
s = 'abaca'
ans = []

get_all_partion(s, [], ans)
print('palindrome partions:', ans)
            

# merge sort

def merge(nums, start, mid, end):
    merge_list = []
    left = start
    right = mid + 1
    
    while left <= mid and right <= end:
        if nums[left] < nums[right]:
            merge_list.append(nums[left])
            left += 1
        else:
            merge_list.append(nums[right])
            right += 1
    
    while left <= mid:
        merge_list.append(nums[left])
        left += 1
    
    while right <= end:
        merge_list.append(nums[right])
        right += 1
    
    for i in range(len(merge_list)):
        nums[i + start] = merge_list[i]
        
    

def merge_sort(nums, start, end):
    if start < end:
        mid = start + (end - start) // 2
        
        merge_sort(nums, start, mid)
        merge_sort(nums, mid + 1, end)
        
        merge(nums, start, mid, end)


nums = [3,4,2,1,6,0,7]

merge_sort(nums, 0, len(nums) - 1)

print('merge sort:', nums)
             

# quick sort

def partion(nums, start, end):
    idx = start - 1
    for j in range(start, end):
        if nums[j] <= nums[end]:
            idx += 1
            nums[j],nums[idx] = nums[idx], nums[j]
    
    idx += 1
    nums[end], nums[idx] = nums[idx], nums[end]
    
    return idx

def quicksort(nums, start, end):
    if start < end:
        pivot = partion(nums, start, end)
        quicksort(nums, start, pivot - 1)
        quicksort(nums, pivot + 1, end)
    

nums = [3,4,2,1,6,0,7]

quicksort(nums, 0, len(nums) - 1)

print('quick sort:', nums)


# count inversion

def inversion_merge(nums, start, mid, end):
    left = start
    right = mid + 1
    merge_list = []
    inversion_count = 0
    
    while left <= mid and right <= end:
        if nums[left] <= nums[right]:
            merge_list.append(nums[left])
            left += 1
        else:
            inversion_count += (mid - left) + 1
            merge_list.append(nums[right])
            right += 1
    
    while left <= mid:
        merge_list.append(nums[left])
        left += 1
    while right <= end:
        merge_list.append(nums[right])
        right += 1
    
    for i in range(len(merge_list)):
        nums[i+start] = merge_list[i]
    
    return inversion_count


def inversion_merge_sort(nums, start, end):
    if start < end:
        mid = start + (end - start) // 2
        
        left_inversion = inversion_merge_sort(nums, start, mid)
        right_inversion = inversion_merge_sort(nums, mid + 1, end)
        
        current_inversion = inversion_merge(nums, start, mid, end)
        
        return left_inversion + right_inversion + current_inversion
    return 0

# nums = [6,3,5,2,7]
nums = [1,3,5,10,2,6,8,9]

print("count_inversion:", inversion_merge_sort(nums, 0, len(nums)-1))
            

# Check Knight Tour Configuration

def canMove(num, row, col, n):
    top_v_r = row - 2
    down_v_r = row + 2
    v_l_c = col - 1
    v_r_c = col + 1

    left_h_c = col - 2
    right_h_c = col + 2
    h_t_r = row - 1
    h_d_r = row + 1

    if top_v_r > -1 and v_l_c > -1 and grid[top_v_r][v_l_c] == num:
        return True, top_v_r, v_l_c
    elif top_v_r > -1 and v_r_c < n and grid[top_v_r][v_r_c] == num:
        return True, top_v_r, v_r_c
    elif down_v_r < n and v_l_c > -1 and grid[down_v_r][v_l_c] == num:
        return True, down_v_r, v_l_c
    elif down_v_r < n and v_r_c < n and grid[down_v_r][v_r_c] == num:
        return True, down_v_r, v_r_c

    elif left_h_c > -1 and h_t_r > -1 and grid[h_t_r][left_h_c] == num:
        return True, h_t_r, left_h_c
    elif left_h_c > -1 and h_d_r < n and grid[h_d_r][left_h_c] == num:
        return True, h_d_r, left_h_c
    elif right_h_c < n and h_t_r > -1 and grid[h_t_r][right_h_c] == num:
        return True, h_t_r, right_h_c
    elif right_h_c < n and h_d_r < n and grid[h_d_r][right_h_c] == num:
        return True, h_d_r, right_h_c
    else:
        return False, 0, 0
    

def check(num, row, col, n):
    if num == n * n - 1:
        return True
    
    can, newRow, newCol = canMove(num+1, row, col, n)
    if can:
        return check(num+1, newRow, newCol, n)
    return False

grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]

if grid[0][0] == 0:
    print(check(0,0,0, len(grid)))