import copy
def minimumBribes(q):
    e = copy.deepcopy(q)
    count = 0
    for i in range(len(q), 0, -1):
        for j in range(1, i):
            if q[j] < q[j - 1]:
                q[j], q[j - 1] = q[j - 1], q[j]
                count += 1

    e.sort()
    if count > len(q) - 1:
        print("Too Chaotic")
        exit()
    if e == q:
        print(count)

q = [5, 1, 2, 3, 7, 8, 6, 4]


print(minimumBribes(q))