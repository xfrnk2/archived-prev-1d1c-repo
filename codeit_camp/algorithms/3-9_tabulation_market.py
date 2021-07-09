def max_profit(price_list, count):
    dp = [0] * (count + 1)

    '''규칙을 정해본다.
    3번째 원소는, 1+2 또는 3의 최댓값이다
    4번재 원소는, 1+3 또는 2+2 또는 4의 최댓값이다.
    -> 현재 번호가 i라고 한다면,
    만약 count가 가격리스트의 전체크기보다 작다면 비교 대상에 price_list[i]를 
    넣고,
    그렇지 않다면 1부터 count//2+1 까지 순회해서, -> 1, 2
    순회 값이 j라고 할때 [i-j + j, ... 최종 순회까지 한 것들중 최댓값이 
    dp[i]의 값이 된다.

    '''

    for i in range(1, count + 1):
        temp = []
        if i < len(price_list):
            temp.append(price_list[i])
        for j in range(1, i // 2 + 1):
            temp.append(dp[i - j] + dp[j])
        dp[i] = max(temp)
    return dp[count]


# 테스트
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
