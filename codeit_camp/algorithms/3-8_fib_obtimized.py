def fib_optimized(n):
    # 코드를 작성하세요
    prev, current = 1, 1
    for _ in range(3, n + 1):
        current, prev = prev + current, current
    return current

# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
