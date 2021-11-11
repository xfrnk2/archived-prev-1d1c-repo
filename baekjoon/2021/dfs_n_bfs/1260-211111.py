# https://www.acmicpc.net/problem/1260



N, M, V = map(int, input().split())
print(N, M, V)
node = [[] for _ in range(M)]
visits = [0] * M


for _ in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)


def bfs():
    q = [V]
    result = []

    while q:
        y = q.pop(0)
        result.append(y)
        visits[y] = 1
        for n in node[y]:
            if visits[n] == 1:
                continue
            q.append(n)
            break
    return result


def dfs():
    visits = [0] * M
    result = []

    def search(n):
        if len(result) == M-1:
            return

        for e in node[n]:
            if visits[e] == 1:
                continue
            visits[e] = 1
            result.append(e)
            search(e)
    for i in range(V, M):
        if visits[i] == 0:
            visits[i] = 1
            result.append(i)
            search(i)

    search(V)
    return result





print(bfs())
print(dfs())