v =[[3, 1], [1, 1], [3, 2]]

def solution(v):
    n1 = []
    n2 = []
    n1v = n2v = None
    r1 = r2 = None
    result = ''
    for x in range(3):
        n1.append(v[x][0])
        n2.append(v[x][1])

    for y in range(2):
        if n1.count(n1[y]) == 2:
            n1v = n1[y]
        if n2.count(n2[y]) == 2:
            n2v = n2[y]

    target = [n1v, n2v]


    setted = [y for x in v for y in x]
    setted = list(set(setted))
    if len(setted) <= 2:
        result = [n2v, n1v]

    else:
        point = v.index(target)

        if v[point][0] != v[point - 1][0]:
            r1 = v[point - 1][0]
        if v[point][0] != v[point + 1][0]:
            r1 = v[point + 1][0]

        if v[point][1] != v[point - 1][1]:
            r2 = v[point - 1][1]
        if v[point][1] != v[point + 1][1]:
            r2 = v[point + 1][1]

        result = [r1, r2]

    return result


solution(v)

