def fairRations(C):
    length = len(C)

    c = 0
    task = 0

    if length == 1:
        return 1

    if length == 2:
        if C[0] % 2 == 0 and C[1] % 2 == 0:
            return c
        elif C[0] % 2 == 1 and C[1] % 2 == 1:
            c += 2
            return c
        else:
            return "NO"

    for x in range(length - 1, 0, -1):

        # if C[x] % 2 == 0 and C[x-1] % 2 == 0:
        #     task += 1
        #     if task == 2:
        #         return "NO"
        #     continue
        # task = 0
        if C[x] % 2 == 1 and C[x - 1] % 2 == 1:
            C[x], C[x - 1] = C[x] + 1, C[x - 1] + 1
            c += 2
        if C[x] % 2 == 1 and C[x - 1] % 2 == 0:
            C[x], C[x - 1] = C[x] + 1, C[x - 1] + 1
            c += 2
        if C[x] % 2 == 0 and C[x - 1] % 2 == 1:
            continue
    return c

