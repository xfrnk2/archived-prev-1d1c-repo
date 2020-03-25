from Algorithm.sort_heap_sort import max_heapify


def max_heap_insert(arr, value):
    current_index = len(arr)
    arr.append(value)

    parent_index = (current_index + 1) // 2 - 1
    while 0 < current_index and arr[current_index] > arr[parent_index]:
        arr[current_index], arr[parent_index] = arr[parent_index], arr[current_index]
        current_index = parent_index
        parent_index = (current_index + 1) // 2 - 1

arr = [16, 8, 15, 5, 7, 13, 14, 2, 4]
max_heap_insert(arr, 10)
print(arr)



def extract_max(arr):
    size = len(arr)
    if size < 1:
        print("error")
    arr[0], arr[size-1] = arr[size-1], arr[0]
    arr.pop()
    max_heapify(arr, 0, size-1)

extract_max(arr)
print(arr)