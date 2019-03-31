import copy
def minimumBribes(q):
    q = list(q)
    original = copy.deepcopy(q)
    s = q.index(1)
    m = q.index(max(q))

    m_c = len(q) - (m + 1)
    s_c = s
    counts = 0

    while m_c > 0:

        q[m], q[m + 1] = q[m + 1], q[m]
        m += 1
        m_c -= 1
        counts += 1

    while s_c > 0:

        q[s], q[s - 1] = q[s - 1], q[s]
        s -= 1
        s_c -= 1
        counts += 1

    original.sort()
    if q == original:
        return counts
    else:
        return 'Too chaotic'

q = 2, 5, 1, 3, 4

print(minimumBribes(q))