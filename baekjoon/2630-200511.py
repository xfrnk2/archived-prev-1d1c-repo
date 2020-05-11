#링크 : https://www.acmicpc.net/problem/2630
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

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int,input().split())))

    origami_func(arr, 0, 0, n)
    print(white)
    print(blue)