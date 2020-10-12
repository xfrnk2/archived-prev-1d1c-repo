# https://programmers.co.kr/learn/courses/30/lessons/42746
def solution(numbers):
    numbers = map(str, numbers)
    answer = ''.join(sorted(numbers, reverse=True, key=lambda n: (n[0], n[1 % len(n)], n[2 % len(n)], n[3 % len(n)])))
    return answer if int(answer) else '0'