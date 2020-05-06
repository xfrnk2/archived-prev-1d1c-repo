#링크 : https://www.acmicpc.net/problem/14494

def dp_func(values):
    n, m = values
    arr = [[0 for _ in range(m+1)] for _ in range(n+1)]
    arr[1][1] = 1
    mod = 1e9+7
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i*j != 1:
                arr[i][j] = (arr[i-1][j]%mod + arr[i][j-1]%mod + arr[i-1][j-1]%mod)%mod
    print(int(arr[n][m]%mod))
dp_func(list(map(int, input().split())))

def another_dp_func(values):
    n, m = values
    mod = 1e9+7
    arr = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i * j == 0:
                arr[i][j] = 1
            else:
                arr[i][j] = (arr[i-1][j]%mod + arr[i][j-1]%mod + arr[i-1][j-1]%mod)%mod
    print(int(arr[n-1][m-1]%mod))
another_dp_func(list(map(int, input().split())))

