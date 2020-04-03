
def counting_sort(arr):
    array_length = len(arr)
    max_value = 0
    values = [0 for _ in range(array_length)]

    for x in arr:
        if max_value < x :
            max_value = x
        values[x] += 1

    # if max_value < array_length:#생각
    #
    result = []
    for value, value_count in enumerate(values):

        if value_count != 0:
            while 0 < value_count:
                result.append(value)
                value_count -=1
    print(result)

arr = [1, 4, 2, 3, 5, 3]
counting_sort(arr)