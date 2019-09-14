def fairRations(B):
    length = len(B)
    count = 0
    for x in range(length - 1, 0, -1):

        if B[x] % 2 == 0 and B[x - 1] % 2 == 0:
            continue
        if B[x] % 2 == 1 and B[x - 1] % 2 == 1:
            B[x], B[x - 1] = B[x] + 1, B[x - 1] + 1
            count += 2
            continue
        if B[x] % 2 == 1 and B[x - 1] % 2 == 0:
            B[x], B[x - 1] = B[x] + 1, B[x - 1] + 1
            count += 2
    if B[0] % 2 == 1:
        return "NO"
    else:
        return count


