
# python에 list는 크기가 가변적이고 어떤 원소 타입이던 저장할 수 있다는 장점이 있습니다. 대신 C의 array보다 메모리를 더 많이 필요로 한다는 단점이 있지요
#
# array.array는 C의 array랑 같다고 보면 됩니다. 같은 타입에 원소만 저장할 수 있는 대신, 메모리를 훨씬 적게 씁니다.


import random

def bubble_sort(arr):
    for i in range(len(arr), 0, -1):
        for j in range(1, i):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1] , arr[j]


    # for i in range(len(arr) - 1, 0, -1):
    #     for j in range(i):
    #         if arr[j] > arr[j + 1]:
    #             arr[j], arr[j + 1] = arr[j + 1], arr[j]


def main():
    rand_list = []
    for _ in range(10):
        rand_list.append(random.randint(1, 10))
    print(rand_list)

    bubble_sort(rand_list)
    print(rand_list)

main()

