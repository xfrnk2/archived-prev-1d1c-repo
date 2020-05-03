def fibo_tail(n: int, lhs, rhs) -> int:
    if n == 1:
        return rhs
    return fibo_tail(n-1, rhs, lhs+rhs)
print(fibo_tail(13, 0, 1))

def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(13))

def fibonacci_w(n: int) -> int:
    if n < 2:
        return 0

    lhs, rhs = 0, 1
    while 1 < n:
        lhs, rhs = rhs, lhs + rhs
        n -= 1
    return rhs


print(fibonacci_w(13))

def fibonacci_f(n:int) -> int:
    if n < 2:
        return 0
    lhs, rhs = 0, 1
    for x in range(2, n+1):
        lhs, rhs = rhs, lhs +rhs
    return rhs
print(fibonacci_f(13))