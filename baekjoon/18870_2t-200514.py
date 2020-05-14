input()
arr = list(map(int, input().split()))
another_arr = sorted(set(arr))
value_indices = {}
for i,j in enumerate(another_arr):
    value_indices[j] = i
for x in arr:
    print(value_indices[x], end=' ')