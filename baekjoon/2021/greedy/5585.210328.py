#https://www.acmicpc.net/problem/5585
'''
소요시간 : 10분
결과 : 성공
'''
def func(money):

    arr = [500, 100, 50, 10, 5, 1]
    answer = 0
    money = 1000 - money  # 480 & 520

    i = 0
    while 0 <= i <= 5:
        m, n = divmod(money, arr[i])
        answer += m
        money = n
        i += 1

    return answer

print(func(int(input())))
