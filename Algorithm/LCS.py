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

def lcs2(a, b):
    arr = [[] for _ in range(len(a)) for _ in range(len(b))]

    for x in range(len(a)):
        for y in range(len(b)):
            if a[x] == 0 or b[y] == 0:
                arr[x][y] = 0
            elif a[x] == b[y]:
                arr[x][y] = arr[x-1][y-1]
            elif a[x] != b[y]:
                arr[x][y] = max(a[x-1][y], a[x][y-1])
    return arr[-1][-1]

print(lcs(S1, S2))








