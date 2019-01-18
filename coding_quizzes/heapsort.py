def heap_sort(array, size, index):
    largest = index
    left_index = index * 2 + 1
    right_index = index * 2 + 2

    if left_index <= size and array[left_index] > array[index]:
        largest = left_index
    else:
        pass
    if right_index <= size and array[right_index] > array[largest]:
        largest = right_index

    if largest != index:
        temp = array[largest]
        array[largest] = array[index]
        array[index] = temp
        heap_sort(array, size, index)


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = 0
size = len(array)

heap_sort(array, size, index)
print(array)