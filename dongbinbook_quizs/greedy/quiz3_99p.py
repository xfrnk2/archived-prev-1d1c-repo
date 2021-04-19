#int(f) - f == 0 소수인지
n, k = map(int, input().split())
count = 0

# 1회차 풀이
# while 1 < n:
#     if n % k == 0:
#         n //= k
#     else:
#         n -= 1
#     count += 1
# print(count)


# input e.g.
# 13 3
# 8 7
#7 7

# 2회차 풀이
while 1 < n:
    n, j = divmod(n, k)
    count += (j + 1)
print(count)