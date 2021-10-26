# lv2

# 나의 풀이 - dfs
def solution(numbers, target):
    ans = 0

    def func(num, level):
        nonlocal ans

        if level == len(numbers):
            if target == num:
                ans += 1
            return

        if level == 1:
            func(- num + numbers[level], level + 1)
            func(- num - numbers[level], level + 1)

        func(num + numbers[level], level + 1)
        func(num - numbers[level], level + 1)

    func(numbers[0], 1)
    return ans

# 나의 풀이 - bfs
from collections import deque


def solution(numbers, target):
    ans = 0

    queue = deque()
    queue.append((numbers[0], 1))

    while queue:
        n, l = queue.popleft()
        if l == len(numbers):
            if target == n:
                ans += 1
            continue

        if l == 1:
            queue.append((-n + numbers[l], l + 1))
            queue.append((-n - numbers[l], l + 1))
        queue.append((n + numbers[l], l + 1))
        queue.append((n - numbers[l], l + 1))
    return ans

# 뇌가 섹시해지는 누군가의 풀이
from collections import deque


def solution(numbers, target):
    ans = 0

    queue = deque()
    queue.append((0, 0))

    while queue:
        n, l = queue.popleft()
        if l > len(numbers):
            break
        elif l == len(numbers) and n == target:
            ans += 1
        queue.append((n + numbers[l - 1], l + 1))
        queue.append((n - numbers[l - 1], l + 1))

    return ans

# 요약 - bfs에서 queue보단 deque, 성능 : 재귀도 성능이 준수, 나의 풀이 dfs(재귀) > 나의 풀이 bfs > 누군가의 풀이