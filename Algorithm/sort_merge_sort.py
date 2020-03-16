def merge_sort(arr):
    if 1 < len(arr):
        mid = len(arr)//2
        l = arr[:mid]
        r = arr[mid:]

        left = merge_sort(l)
        right = merge_sort(r)

        return merge(left, right)
    return arr

def merge(left, right):
    i, j, temp = 0, 0, []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            temp.append(left[i])
            i +=1
        else:
            temp.append(right[j])
            j += 1
    while i < len(left):
        temp.append(left[i])
        i+=1
    while j < len(left):
        temp.append(right[j])
        j+=1

    return temp

arr = [5, 3, 4, 100, 2, 1]
print(merge_sort(arr))