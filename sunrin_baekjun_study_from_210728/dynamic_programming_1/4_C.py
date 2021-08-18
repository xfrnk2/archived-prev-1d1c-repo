# https://www.acmicpc.net/problem/2167
# 동적 프로그래밍에 속해있는데, 백준 알고리즘 분류에는 구현이라고.. 게다가 아래 코드는 시간 초과했다. 다시 풀어보자.

# import sys
# N, M = map(int, sys.stdin.readline().split())
#
# arr = []
# for _ in range(N):
#     arr.append(list(map(int, sys.stdin.readline().split())))
#
# K = int(input())
#
# for _ in range(K):
#     i, j, x, y = map(int, sys.stdin.readline().split())
#     # i - 1
#     # x - 1
#     if i == x:
#         print(sum(arr[i - 1][j-1:y]))
#     elif j == y:
#         temp = 0
#         for m in range(i-1, x):
#             temp += arr[m][j-1]
#         print(temp)
#     else:
#         temp = 0
#         for m in range(i-1, x):
#             for n in range(j-1, y):
#                 temp += arr[m][n]
#         print(temp)

# 동적계획법을 통해 풀었다. 어떻게 흘러가는지 전체 흐름을 완벽하게 이해하기 위해 머리를 싸매고 고민했다.
# 그 결과 이해하고 납득하고 어떻게 돌아가는지 머릿속으로 그려볼수는 있을 정도가 됬다. 자포자기 하지 않아서 다행이다. 앞으로
# 이런 유형의 문제가 자주 보일텐데, 하다보면 익숙해 질 거라고 생각이 든다.

import sys
N, M = map(int, sys.stdin.readline().split())
arr = [[0] * (M+1)for _ in range(N+1)]
num = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for i in range(1, N+1):
    for j in range(1, M+1):
        arr[i][j] = num[i-1][j-1] - arr[i-1][j-1] + arr[i-1][j] + arr[i][j-1]

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, sys.stdin.readline().split())
    print(arr[x][y] - arr[x][j-1] - arr[i-1][y] + arr[i-1][j-1])
'''
2 2, 3 4


0 0 0 0
0 1 3 7
0 9 27 63
63 - 27 - 7 + 3

1 2 4
8 16 32



[1, 2, 3, 4],
[5, 6, 7, 8]
[9, 10, 11, 12]

[0, 0, 0, 0, 0],
[0, 1, 3, 6, 10],
[0, 6, 14, 24, 36],
[0, 15, 33, 54, 78]


34
54 - 15 - 6 = 54 - 21 = 33

3 4
1 2 3 4
5 6 7 8
9 10 11 12
3
1 1 2 3
1 2 1 2
1 3 2 3

'''