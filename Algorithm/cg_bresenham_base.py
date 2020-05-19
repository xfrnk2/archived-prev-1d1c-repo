def func(n, point1, point2):
    field = [["."] * n for i in range(n)]

    xs, ys = point1
    xe, ye = point2

    dy, dx = ye - ys, xe - xs # x,y 좌표별 간격의 값
    yv = ys

    if 1 <= dy/dx: #기울기 1 이상
        xv = xs
        f = 2 * dx - dy
        for yvv in range(yv, ye+1):
            print(f, xv, yvv)
            field[yvv][xv] = '@'
            if f < 0:
                f += 2 * dx
            else:
                f += 2 * (dx - dy)
                xv += 1


    elif 0 < dy/dx < 1:
        f = 2 * dy - dx
        for xv in range(xs, xe+1):
            field[yv][xv] = '@'
            if f < 0:
                f += 2 * dy
            else:
                yv -= 1
                f += 2 * (dy - dx)

    else:
        raise Exception('기울기가 음수라면 취급하지 않음')

    for i in field:
        print(i)



if __name__ == "__main__":
    n = int(input())
    point1 = list(map(int, input().split()))
    point2 = list(map(int, input().split()))
    func(n, point1, point2)



'''
10
2 1
5 8 
'''