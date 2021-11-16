# https://www.acmicpc.net/problem/1260
# from collections import defaultdict
#
#
# N, M, V = map(int, input().split())
# print(N, M, V)
# node = [[]for _ in range(N+1)]
# visits = [0] * (N+1)
#
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     node[a].append(b)
#     node[b].append(a)
#
# for n in node:
#     n.sort()
#
# print(node)
#
# def bfs():
#     q = [V]
#     result = []
#
#     while q:
#         y = q.pop(0)
#         result.append(y)
#         visits[y] = 1
#
#         for n in node[y]:
#             if visits[n] == 1:
#                 continue
#             q.append(n)
#
#
#     return result
#
#
# def dfs():
#     visits = [0] * (N+1)
#     result = []
#
#     def search(n):
#         if len(result) == M-1:
#             return
#
#         for e in node[n]:
#             if visits[e] == 1:
#                 continue
#             visits[e] = 1
#             result.append(e)
#             search(e)
#     for i in range(V, M):
#         if visits[i] == 0:
#             visits[i] = 1
#             result.append(i)
#             search(i)
#
#     search(V)
#     return result
#
#
#
#
#
# print(bfs())
# print(dfs())
'''
4 5 1
1 2
1 3
1 4
2 4
3 4

1 2 4 3
1 2 3 4

5 5 3
5 4
5 2
1 2
3 4
3 1

3 1 2 5 4
3 1 4 2 5
'''

# 생각 나는대로 코딩을 하고서는 bfs에서 판단 미스가 있어서 제법 헤맸는데, 결국 방문을 기록하는 순서를 바꾸고 간선을 확인하기 위한 집합을 추가하고 나니 잘 동작하게 되었다.

N, M, V = map(int, input().split())

node = [[] for _ in range(N + 1)]
visits = [0] * (N+1)
visits_set = set()
for _ in range(M):
    s, e = map(int, input().split())
    node[s].append(e)
    node[e].append(s)
    visits_set.add((s, e))
    visits_set.add((e, s))
for i in range(1, len(node)):
    node[i].sort()


def bfs():
    visits_bfs = visits[:]
    queue = [V]
    visits_bfs[V] = 1

    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for value in node[v]:
            if visits_bfs[value] == 0 and (v, value) in visits_set:
                visits_bfs[value] = 1
                queue.append(value)


def dfs():
    visits_dfs = visits[:]

    def search(n):
        if all(visits_dfs):
            return
        if visits_dfs[n]:
            return
        visits_dfs[n] = 1
        print(n, end=' ')
        for v in node[n]:
            if visits_dfs[v] == 0 and (n, v) in visits_set:
                search(v)

    search(V)


dfs()
print()
bfs()

