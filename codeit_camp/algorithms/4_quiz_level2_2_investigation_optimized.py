# 나의 풀이 코드

def sublist_max(profits):
    acc = 0
    cul = 0
    for i in range(len(profits)):
        if profits[i] >= 0:
            acc += profits[i]
            cul = 0
        else:
           if cul == 0:
               cul = acc
           acc += profits[i]
        acc = max(acc, profits[i])

    return max(cul, acc)
# 테스트
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))


# 문제 해설 코드

def sublist_max(profits):
    max_profit_so_far = profits[0]
    max_check = profits[0]
    for i in range(1, len(profits)):
        max_check = max(profits[i], max_check + profits[i])

        max_profit_so_far = max(max_profit_so_far, max_check)
    return max_profit_so_far


# 테스트
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))