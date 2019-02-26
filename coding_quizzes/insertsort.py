import random


def insert_sort(arr):
    for i in range(1, len(arr)):

        for j in range(0, i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                pass

def Main():
    rand_list = []
    for _ in range(1, 10):
        rand_list.append(random.randint(1, 10))
    print(rand_list)

    insert_sort(rand_list)

    print(rand_list)

Main()