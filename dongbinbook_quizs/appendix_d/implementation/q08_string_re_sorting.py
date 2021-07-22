s = ''.join(sorted(input()))
n = 0
p = len(s)
for i in range(len(s)):
    if not s[i].isdecimal():
        p = i
        break
    n += int(s[i])

print(s[p:] + str(n))
