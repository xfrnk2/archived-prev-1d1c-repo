#https://programmers.co.kr/learn/courses/30/lessons/62048


def solution(w, h):
    x = 0
    f = 2*w - h
    df1 = 2* w
    df2 = 2*(w-h)
    stack = []
    for y in range(h):
        stack.append((x, y))
        if f < 0:
            f += df1
        else:
            x += 1
            f += df2
    return stack
print(len(solution(8, 12)))