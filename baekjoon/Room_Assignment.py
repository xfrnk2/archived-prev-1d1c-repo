#https://www.acmicpc.net/problem/1931

from operator import itemgetter
def func(values):
    start_time = value_count = 0
    for value in values:
        if start_time <= value[0]:
            value_count += 1
            start_time = value[1]
    return value_count

if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key=itemgetter(1,0))
    print(func(arr))