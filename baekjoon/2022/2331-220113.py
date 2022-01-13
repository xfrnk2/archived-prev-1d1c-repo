# https://www.acmicpc.net/problem/2331

def get_next_number(current_number, p):
    result = n = 0
    while 0 < current_number:
        current_number, n = divmod(current_number, 10)
        result += n ** p
    return result


def solution():
    A, P = map(int, input().split())
    record = [A]
    current_number = A
    while True:
        next_number = get_next_number(current_number, P)
        try:
            search_result = record.index(next_number)
            return search_result
        except ValueError:
            record.append(next_number)
            current_number = next_number


print(solution())
