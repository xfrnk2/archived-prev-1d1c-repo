def insertion_sort(collection):

    for index in range(1, len(collection)):
        while 0 < index and collection[index] < collection[index - 1]:
            collection[index], collection[
                index - 1] = collection[index - 1], collection[index]
            index -= 1

    return collection

arr = [5, 1, 0, 6, 2, 7, 3, 9, 3, 8, 4]
# print(insertion_sort(arr))


def insertion_sort2(arr):
    for index in range(1, len(arr)):
        while 0 < index and arr[index] < arr[index-1]:
            arr[index], arr[index-1] = arr[index-1], arr[index]
            index -= 1
    return arr
print(insertion_sort2(arr))