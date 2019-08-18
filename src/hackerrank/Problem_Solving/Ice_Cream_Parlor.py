def icecreamParlor(m, arr):
    a_value = b_value = 0
    for i, j in enumerate(arr):
        if (m - j) in arr[i+1:]:
            b_value = m - j
            a_value = i
            continue

        if j == b_value:
            b_value = i
            return (a_value+1, b_value+1)