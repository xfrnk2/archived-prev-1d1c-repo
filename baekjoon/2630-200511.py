#링크 : https://www.acmicpc.net/problem/2630
from itertools import product
import time
white, blue = 0, 0
def origami_func(arr, x, y, n):
    global white, blue
    target = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if target != arr[i][j]:
                origami_func(arr, x, y, n//2)
                origami_func(arr, x, y+n//2, n//2)
                origami_func(arr, x+n//2, y, n//2)
                origami_func(arr, x+n//2, y+n//2, n//2)
                return

    if target == 1:
        blue += 1
        return
    else:
        white += 1
        return

def origami_func2(arr, x, y, n): # product 사용, 이중 for문 -> 1중으로 변경
    global white, blue
    check = [arr[i][j] for i, j in product([v for v in range(x, x+n)], [v for v in range(y, y+n)])]
    if all(check):
        blue += 1
        return
    elif not any(check):
        white += 1
        return
    else:
        origami_func(arr, x, y, n // 2)
        origami_func(arr, x, y + n // 2, n // 2)
        origami_func(arr, x + n // 2, y, n // 2)
        origami_func(arr, x + n // 2, y + n // 2, n // 2)
        return

def origami_func3(arr, x, y, n): #while 문
    global white, blue
    target = arr[x][y]
    i, j = x, y
    while x <= i < x+n and y <= j < y+n:

        if target != arr[i][j]:
            origami_func(arr, x, y, n//2)
            origami_func(arr, x, y+n//2, n//2)
            origami_func(arr, x+n//2, y, n//2)
            origami_func(arr, x+n//2, y+n//2, n//2)
            return
        i, j = i+1, j+1

    if target == 1:
        blue += 1
        return
    else:
        white += 1
        return


if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int,input().split())))

    origami_func2(arr, 0, 0, n)
    for _ in range(10):
        start = time.time()
        for _ in range(5000):
            origami_func(arr, 0, 0, n)
        print("1 : ",time.time() - start)


        start = time.time()
        for _ in range(5000):
            origami_func2(arr, 0, 0, n)
        print("2 : ",time.time() - start)


        start = time.time()
        for _ in range(5000):
            origami_func3(arr, 0, 0, n)
        print("3 : ",time.time() - start)
        print("================")

    print(white)
    print(blue)