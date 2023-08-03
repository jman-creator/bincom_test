# memoization
stored = {1: 0, 2: 1}

def fib(n):
    """
    Get nth Fibonacci number
    """
    if n in stored:
        return stored[n]
    else:
        val = fib(n-1) + fib(n-2)
        stored[n] = val
        return val

fibsum = 0

for i in range(50):
    fibsum += fib(i+1)

print("Sum of first 50: ", fibsum)