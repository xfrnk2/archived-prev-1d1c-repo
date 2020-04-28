#링크 : https://www.acmicpc.net/problem/1003
values = {0: (1, 0), 1: (0, 1)}
def fibonacci_func(n):
    if  len(values) <= n:
        for x in range(2, n+1):
            if not x in values:
                values[x] = (values[x - 2][0] + values[x - 1][0], values[x - 1][1] + values[x - 2][1])
    print(f"{values[n][0]} {values[n][1]}")

if __name__ == "__main__":
    get_input = [int(input()) for _ in range(int(input()))]
    for n in get_input:
        fibonacci_func(n)