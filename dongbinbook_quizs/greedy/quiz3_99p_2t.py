m, n = map(int, input().split())
c = 0
while 1 < m:
    m, j = divmod(m, n)
    c += (1 + j)



print(c)

