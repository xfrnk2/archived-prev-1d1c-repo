n = int(input())
items = list(map(int, input().split()))

for i in range(2, n):
    items[i] = max(items[i-1], items[i-2]+items[i])

print(items[n-1])

'''
input
4
1 3 1 5

output
8



input
6
1 3 1 5 2 6

output
14
'''