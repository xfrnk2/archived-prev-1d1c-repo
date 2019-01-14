import random
def insert_sort(arr):
    for i in range(0, len(arr)):
        if i == 0:
            pass
        key = i

        for j in range(0, i):
            if arr[i] > arr[j]:
                pass
            elif arr[key] < arr[j]:
                target =

        if arr[i - 1] > arr[key]:
            arr[i - 1], arr[key] = arr[key], arr[i - 1]
        elif arr[i - 1] < arr[key]:




def Main():
    rand_list = []
    for _ in range(1, 10):
        rand_list.append(random.randint(1, 10))
    print(rand_list)

    insert_sort(rand_list)

    print(rand_list)

