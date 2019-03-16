def solution(money):
    if not 1 <= money < 1000000:
        print("money가 1 이상 1000000이하의 자연수가 아닙니다.")

    result = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    values = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]
    num = 0

    money = int(money)

    while money > 0:
        if money >= values[num]:
            result[num] += 1
            money = money - values[num]
        else:
            num += 1
    return result


solution(50237)