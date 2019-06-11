#https://www.hackerrank.com/challenges/cut-the-sticks/problem

def cutTheSticks(arr):
    c = len(arr)
    answer = [c]

    if c == 1:
        return answer

    a = sorted(list(set(arr)))
    a.pop(-1)

    for i in a:
        to_cut = list(filter(lambda j: i == j, arr))
        v = c - len(to_cut)
        answer.append(v)
        c = v
    return answer
