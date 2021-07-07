def fib_tab(n):
    fib = [0 for _ in range(n+1)]
    fib[1], fib[2] = 1, 1
    for i in range(3, n+1):
        fib[i] += fib[i-2] + fib[i-1]
    return fib[n]
    # 코드를 작성하세요.

# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))