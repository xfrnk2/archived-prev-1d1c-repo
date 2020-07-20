#https://programmers.co.kr/learn/courses/30/lessons/62048


def solution(w, h):
    m, n = w, h
    while 0 < n:
        m, n = n, m%n
    squares = w+h-1 if m==1 else w+h-m
    return w*h - squares
print(solution(8, 12))
