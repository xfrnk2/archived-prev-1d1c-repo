#https://www.acmicpc.net/problem/3052

arr = [int(input()) for _ in range(10)]
value = list(map(lambda x : x % 42, arr))
print(len(set(value)))