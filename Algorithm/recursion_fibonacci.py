def fibonacci(n: int) -> int:

    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))




def fibo_tail(n : int, lhs: int, rhs: int):

    if n == 1:
        return rhs
    return fibo_tail(n-1, rhs, lhs + rhs)

print(fibo_tail(5, 0, 1))