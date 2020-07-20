array = [20, 60, 10, 70, 30, 50, 40, 80]
n = len(array)  # array의 길이(크기)

def bubble_sort(array):
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def improved_bubble_sort(array):
    for i in range(n - 1, 0, -1):
        #교환이 일어났는지 알 수 있는 변수 = check_exchanged
        check_exchanged = False
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                # 교환이 일어났으므로 check_exchanged = True
                check_exchanged = True

        #교환이 일어나지 않았을 경우 순회를 멈추고 종료
        if not check_exchanged:
            break

    return array