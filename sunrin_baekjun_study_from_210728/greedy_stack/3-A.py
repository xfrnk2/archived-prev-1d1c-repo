# https://www.acmicpc.net/problem/11047


N, K = map(int, input().split())
coin = []
for _ in range(N):
    coin.append(int(input()))
coin.sort(reverse=True)
count = 0
while 1 <= K:
    for i in range(len(coin)):
        a, b = divmod(K, coin[i])
        if 0 < a:
            K = b
            count += a
            continue
print(count)