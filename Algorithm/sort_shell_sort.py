def insertionSort(arr, start, interval):
    for i in range(start+interval, len(arr), interval):
        current_value = arr[i]
        position = i
        while interval <= position and arr[position] < arr[position-interval]:
            arr[position] = arr[position-interval]
            position = position - interval
        arr[position] = current_value

def shellSort(arr):
    interval = len(arr)//2
    while 0 < interval:
        for x in range(interval):
            insertionSort(arr, x, interval)
            print(arr)
        interval = interval//2

shellSort([1, 5, 20, 4, 7, 2, 8, 9])






arr = [0, 8, 11, 6, 2, 13, 7, 30]
shellSort(arr)