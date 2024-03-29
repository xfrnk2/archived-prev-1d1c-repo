def power(x, y):
    '''
    y가 5라면
    y//2 + 1만큼 반복한다 -> 3회 반복 필요
    y가 6이라면
    y//2 만큼 반복한다 -> 3회 반복 필요
    y가 7이라면
    y//2 + 1 만큼 반복한다 -> 4회 반복 필요

    홀수라면 +1회, 짝수라면 그대로.

    기억공간을 위에서 구한 값 - 1개만큼 만든다.

    y//2를 넘어가기 전까지만 반복하여 기억공간을 채운다.
    가져온다.

    '''

    d = [0] * (y + 1)
    d[0] = 1
    mid = y // 2
    for i in range(1, mid+2):
        d[i] = d[i - 1] * x

    return d[mid] * d[y - mid]


# 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))