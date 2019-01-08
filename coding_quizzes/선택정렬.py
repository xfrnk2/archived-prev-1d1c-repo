# 주어진 배열 중에서 최솟값을 찾는다.
# 그 값을 맨 앞에 위치한 값과 교체한다(패스(pass)).
# 맨 처음 위치를 뺀 나머지 리스트를 같은 방법으로 교체한다.
# 하나의 원소만 남을 때까지 위의 1~3 과정을 반복한다.

import random
#
# def selected_sort(random_list):
#   for sel in range( len(random_list)-1 ): // 총 길이의 - 1 횟수만큼 동작한다
#     min = random_list[sel] // 해당 순서
#     minindex = sel // 해당 순서의 인덱스
#     # find min value
#     for step in range( sel+1, len(random_list) ): // 가장 앞에서부터 두번째 인덱스~ 마지막 값까지 반복하는 반복문이다.
#       if min > random_list[step]: // min(선
#         min = random_list[step]
#         minindex = step
#     # swap
#     random_list[minindex] = random_list[sel]
#     random_list[sel] = min
#
# def Main():
#   list = []
#   for i in range(10):
#     list.append( random.randint(1,10) )
#   print("< Before Sort >")
#   print(list)
#
#   selected_sort(list) # now sorting!
#   print("< After Sort >")
#   print(list)
#
# Main()
import random
def sel_sort(rand_list):
    for sel in range(0, len(rand_list) - 1):
        minvalue = sel
        for loop in range(sel + 1, len(rand_list)):
            if rand_list[loop] < rand_list[sel]:
                minvalue = loop
        temp = rand_list[minvalue]
        rand_list[minvalue] = rand_list[sel]
        rand_list[sel] = temp

def Main():
    rand_list = []
    for _ in range(1, 10):
        rand_list.append(random.randint(1, 10))
    print(rand_list)

    sel_sort(rand_list)

    print(rand_list)

Main()