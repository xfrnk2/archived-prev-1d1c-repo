arr = ['a', 'b', 'c', 'd']
length = len(arr)
bool_list = [[] for _ in range(length)]

result = []


def powerset(k: int):
    if k == length:
        value = ''
        for x in range(k):
            if bool_list[x]:
                value += arr[x]
        result.append(value)

    else:
        bool_list[k] = []
        powerset(k + 1)
        bool_list[k] = [1]
        powerset(k + 1)


powerset(0)
print(result)
