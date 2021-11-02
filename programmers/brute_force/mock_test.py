def solution(answers):
    N = len(answers)
    d1 = [1, 2, 3, 4, 5] * (N // 5 + 1)
    d2 = [2, 1, 2, 3, 2, 4, 2, 5] * (N // 8 + 1)
    d3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (N // 10 + 1)

    user = [0] * 3
    for i in range(len(answers)):
        if d1[i] == answers[i]:
            user[0] += 1
        if d2[i] == answers[i]:
            user[1] += 1
        if d3[i] == answers[i]:
            user[2] += 1

    m = max(user)
    ans = []
    for i, u in enumerate(user):
        if u == m:
            ans.append(i + 1)
    return ans

from itertools import permutations
arr = "011"
dp = set(permutations(arr, 3))
for d in dp:
    print(''.join(d))