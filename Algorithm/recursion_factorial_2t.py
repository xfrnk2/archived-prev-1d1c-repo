# while문을 사용한 factorial 구현
def factorial_w(n):
    if n == 0:
        return n
    result = 1
    while 1 < n:
        result *= n
        n-=1
    return result
print([factorial_w(x) for x in range(9)])
# for문을 사용한 factorial 구현
def factorial_f(n):
    if n == 0:
        return n
    result = 1
    for x in range(2, n+1):
        result *= x
    return result
print(factorial_f(5))
# recursive하게 구현
def factorial_r(n):
    if 0 <= n < 2:
        return 1
    return n * factorial_r(n-1)
print(factorial_r(6))