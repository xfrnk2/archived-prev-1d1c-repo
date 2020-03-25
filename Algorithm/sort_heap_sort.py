# 조건 1. 유일하게 루트 노드만이 'heap-property; 자식노드가 부모노드보다 작거나 같다'를 만족하지 않는다.
# 조건 2. 트리 모양은 complete-binary-tree 여야 하고, 왼쪽 서브트리와 오른쪽 서브트리가 그들 자체로 'heap'인 상태이다.
# 위와 같은 조건에서 'max-heap'을 만들어 주는 함수를 아래의 heapify(arr,i)로 구현한다.

def max_heapify(arr, current_index, size):
    left_child_index, right_child_index = (current_index+1)*2-1, (current_index+1)*2
    target_index = left_child_index

    # 자식 노드가 없을 경우 종료한다.
    if size - current_index <= 2:
        return

    # 왼쪽 노드만 있는 경우 1:1 비교연산을 한다.
    elif size == 2 * (current_index + 1):
        if arr[current_index] < arr[target_index]:
            arr[current_index], arr[target_index] = arr[target_index], arr[current_index]
        return

    #자식노드 중 더 큰 값을 가진 쪽의 인덱스를 'target_index'에 저장한다.
    if arr[left_child_index] < arr[right_child_index]:
        target_index = right_child_index

    #'target_index'에 위치한 값과 'current_index'에 위치한 값을 비교 연산을 통해 스왑한다.
    if arr[current_index] < arr[target_index]:
        arr[target_index], arr[current_index] = arr[current_index], arr[target_index]
        return max_heapify(arr, target_index, size)

    #자식 노드가 전부 루트 노드보다 작은 값일 경우 종료한다.
    else:
        return


def heap_sort(arr, size):
    #배열 arr 를 'max-heap'화 한다.
    max_heapify(arr, 0, len(arr))
    #'max-heap'을 출력한다.
    print(arr)

    #size-1번 순회한다.
    for max_index in range(size-1, 0, -1):
        arr[max_index], arr[0] = arr[0], arr[max_index]
        #제일 마지막 위치에 최댓값이 저장되면 더이상 비교연산이 필요없어지므로 전체 범위(size)를 'max_index'로 한다.
        max_heapify(arr, 0, max_index)


arr = [4, 16, 15, 8, 7, 13, 14, 2, 5]
heap_sort(arr, len(arr))
print(arr)
