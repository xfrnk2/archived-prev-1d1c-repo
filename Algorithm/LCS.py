def lcs(a, b):
    prev = [0]*len(a)
    for i,r in enumerate(a):
        current = []
        for j,c in enumerate(b):
            if r==c:
                e = prev[j-1]+1 if i* j > 0 else 1
            else:
                e = max(prev[j] if i > 0 else 0, current[-1] if j > 0 else 0)
            current.append(e)
        prev = current
    return prev[-1]

S1 = "THESTRINGS" # ans = 5
S2 = "THISISIT"
# S1 = "ABCDA" # ans = 4
# S2 = "ACBDEA"
print(lcs(S1, S2))

def lcs_standard(lhs, rhs):
    if lhs < rhs:
        lhs, rhs = rhs, lhs

    m, n = len(lhs), len(rhs)

    arr = [[0]*(n+1) for _ in range(m+1)]

    for x in range(m+1):
        for y in range(n+1):
            if x == 0 or y == 0:
                arr[x][y] = 0
            elif lhs[x-1] == rhs[y-1]:
                arr[x][y] = arr[x-1][y-1] + 1
            elif lhs[x-1] != rhs[y-1]:
                arr[x][y] = max(arr[x-1][y], arr[x][y-1])
    return arr[m][n]

print(lcs_standard(S1, S2))






