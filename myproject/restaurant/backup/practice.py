result = 0
group = [5, 10, 15]
waiting_queue = [15, 20, 25, 0] #마지막 에는 새로 들어오는 값의 자리를 메꾸기 위함인건고 아무 값이나 들어와도 결과는 같다.


while waiting_queue:
    group.sort()
    target = group.pop(0)
    result += target
    group = [i - target for i in group]

    group.append(waiting_queue.pop(0))
    print(group)

print(result)


bbb = ccc = []



# #같지만 초기에 짠 코드, 지금은 이 상태로부터 순서가 변경되었음
# while waiting_queue:
#     target = group.pop(0)
#     result += target
#     group = [i - target for i in group]
#
#     group.append(waiting_queue.pop(0))
#     group.sort()
#     print(group)
#
# print(result)
