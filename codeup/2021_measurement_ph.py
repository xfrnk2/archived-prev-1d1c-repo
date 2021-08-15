length = int(input())

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


dic = dict()
for _ in range(length):
    i = int(input())
    dic[i] = dic.get(i, 0) + 1

new_dic = dict()
for i, j in dic.items():
    if new_dic.get(j):
        new_dic[j] += [i]
    else:
        new_dic[j] = [i]
print(new_dic)

a = merge_sort(list(new_dic.keys()))
fv, sv = new_dic[a[-1]], new_dic[a[-2]]
m = merge_sort(fv)
print(fv, m)
if len(list(new_dic.keys())) <= 1:
    print(max(abs(m[-1]-m[-2]), abs(m[-1]-m[0])))
else:
    n = merge_sort(sv)
    print(max(abs(m[-1] - n[-1]), abs(m[-1] - n[0])))
