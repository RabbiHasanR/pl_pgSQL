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



