def staircase(n):
    prev, current = 1, 1

    for i in range(2, n + 1):
        prev, current = current, prev + current
    return current


# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))
