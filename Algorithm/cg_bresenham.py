def func(n, x, y):
    field = [["."] * n for i in range(n)]

    xs, ys = x
    xe, ye = y
    yv = ys
    h, w = ye - ys, xe - xs
    f = 2 * h - w
    df1 = 2 * h
    df2 = 2 * (h - w)

    for xv in range(xs, xe+1):
        field[yv][xv] = '@'
        if f < 0:
            f += df1
        else:
            yv += 1
            f += df2


    for i in field:
        print(i)



if __name__ == "__main__":
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    func(n, x, y)



'''
10
1 1
6 4
'''