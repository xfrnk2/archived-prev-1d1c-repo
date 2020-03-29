
#가운데 값을 피벗으로 하는 퀵 정렬을 구현해본다.
def quick_sort(arr, left, right):
    lhs, rhs = left, right
    pivot = arr[(left+right)//2]
    #아래의 while문을 통하여 pivot 기준으로 좌, 우 크고 작은 값을 나열한다.
    while lhs <= rhs:
    #pivot이 중간 값이고, 비교 대상 arr[lhs], arr[rhs]는 pivot과 비교하니 중간 지점을 넘어가면 종료라 볼 수 있음.
        while arr[lhs] < pivot: # left부터 증가하며 pivot 이상의 값을 찾음
            lhs+=1
        while arr[rhs] > pivot: # right부터 감소하며 pivot 이하의 값을 찾음
            rhs-=1
        if lhs <= rhs: # 현재 lhs이 rhs이하면 (이유 : lhs>rhs 부분은 이미 정리가 된 상태임).

            if lhs!= rhs: # 같지 않은 경우만
                arr[lhs], arr[rhs] = arr[rhs], arr[lhs] #lhs와 rhs가 같다면 교환은 필요 없으므로 한 칸 씩 진행
            #lhs, rhs 한칸 더 진행
            lhs+=1
            rhs-=1
    #조건 확인하여 재귀함수로
    if left < rhs:
        quick_sort(arr, left, rhs)
    if lhs < right:
        quick_sort(arr, lhs, right)

# arr = [2, 9, 4, 18, 5, 1, 7, 8, 15, 12]
arr = [60, 200, 30, 0, 250, 70, 11, 5]
quick_sort(arr, 0, len(arr)-1)



print(arr)