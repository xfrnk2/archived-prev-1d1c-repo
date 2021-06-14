import timeit

n, m = map(int, input().split())
items = list(map(int, input().split()))

start = min(items)
end = max(items)
result = 0

while start <= end:
    mid = (start+end)//2
    quantity = 0
    for item in items:
        if mid < item:
            quantity += item - mid
    if quantity < m:
        end -= 1
    else:
        result = mid
        start += 1

print(result)

'''
input
4 6
19 15 10 17

output
15
'''
