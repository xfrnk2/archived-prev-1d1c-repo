def insertionSort(arr, start, interval):
    for i in range(start, len(arr), interval):
        current_value = arr[i]
        while interval <= i and arr[i] < arr[i-interval]:
            arr[i] = arr[i-interval]
            arr[i-interval] = current_value

def shellSort(arr):
    interval = len(arr)//2
    while 1 <= interval:
        for x in range(interval):
            insertionSort(arr, x, interval)
            print(arr)
        interval = interval//2








arr = [0, 8, 11, 6, 2, 13, 7, 30]
print(shellSort(arr))