#링크 : https://www.acmicpc.net/problem/14494

def dp_func(n, m):

    arr = [[0 for _ in range(m+1)] for _ in range(n+1)]
    arr[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i*j != 1:
                arr[i][j] = arr[i-1][j] + arr[i][j-1] + arr[i-1][j-1]
    print(arr[n][m])
dp_func(4, 5)


