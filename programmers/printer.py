#https://programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities, location):
    data_queue = [(i, j) for i, j in enumerate(priorities)]
    target, count = data_queue[location], 1

    while 1 < len(data_queue):
        J = data_queue.pop(0)
        if any(J[1] < x[1] for x in data_queue):
            data_queue.append(J)
        else:
            if J == target: break
            count += 1
    return count

print(solution([2,1,3,2], 2))

