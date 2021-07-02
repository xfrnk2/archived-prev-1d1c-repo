# https://programmers.co.kr/learn/courses/30/lessons/60061?language=python3
# 삭제에 대해 감이 안잡혔는데 해설을 보고 이해했다. 아래는 해답 코드이다.
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            if y == 0 or (x - 1, y, 1) in answer or (x, y, 1) in answer or (x, y - 1, 0) in answer:
                continue
            return False
        elif stuff == 1:
            if (x, y - 1, 0) in answer or (x + 1, y - 1, 0) in answer or (
                    (x - 1, y, 1) in answer and (x + 1, y, 1) in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []

    for s in build_frame:
        x, y, stuff, operate = s
        if operate == 0:
            answer.remove((x, y, stuff))
            if not possible(answer):
                answer.append((x, y, stuff))
        if operate == 1:
            answer.append((x, y, stuff))
            if not possible(answer):
                answer.remove((x, y, stuff))
    return sorted(answer)