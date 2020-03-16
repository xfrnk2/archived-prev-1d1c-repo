def divide(arr):
    if 1 < len(arr):
        mid = len(arr)//2
        left, right = arr[:mid], arr[mid:]

        lhs, rhs = divide(left), divide(right)
        return conquer(lhs, rhs)
    else:
       return arr

def conquer(left, right):
    i, j, temp = 0, 0, []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1
    if i < len(left):
        temp.extend(left[i:])
    else:
        temp.extend(right[j:])
    return temp

arr = [6, 5, 4, 3, 3, 100, 7, 2, 1]
print(divide(arr))