#https://app.codesignal.com/arcade/intro/level-2/yuGuHvcCaFCKk56rJ
def shapeArea(n):
    if n <= 1:
        return n
    result = 1+4*(n-1)
    if 2 < n:
        while 0 < n-2:
            result += (n-2)*4
            n -= 1
    return result

#문제 해결후 조회해 볼 수 있는 다른 사람 코드중 추천수가 높았던 코드
def shapeArea2(n):
    return n ** 2 + (n - 1) ** 2


