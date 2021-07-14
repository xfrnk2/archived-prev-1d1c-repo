#  최대 수익률을 찾으라
# 풀이하는데 30분 소요됨, 왜 돌아가지? 의문.. 100% 납득은 안되는 코드.

def max_profit(stock_list):
    min_value = stock_list[0]
    value = stock_list[1] - stock_list[0]
    for i in range(1, len(stock_list)):
        value = max(value, stock_list[i] - stock_list[i - 1], stock_list[i] - min_value)
        if stock_list[i] < min_value:
            min_value = stock_list[i]
    return value

    # 낮은거에서 높은거로가는 큰거
    # 높은거에서 작은거로가는 작은거


# 테스트
print(max_profit([7, 1, 5, 3, 6, 4])) # 1에 사서 6에서 팔면 최대 수익률인 5를 얻는다.
print(max_profit([7, 6, 4, 3, 1])) # 7에서 사서 6에서 팔면 최대 수익률인 -1을 얻는다.
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))