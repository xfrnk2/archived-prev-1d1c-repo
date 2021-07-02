def fib_memo(n, cache):
    # 코드를 작성하세요.
    cache[1] = 1
    cache[2] = 1
    for i in range(3, n+1):
        cache[i] = cache[i-2] + cache[i-1]
    return cache[n]
def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)


# 테스트
print(fib(10))
print(fib(50))
print(fib(100))