# AT TEST WITH JS: TODO - 2. 연속된 숫자들의 최대합 구하기



def solution (numbers):
    arr = list(map(int, numbers.split(' ')))

    dp = [arr[0]] + [0] * (len(arr)-1)

    for i in range(1, len(arr)):
        if arr[i] < dp[i-1] + arr[i]:
            dp[i] = dp[i-1] + arr[i]
        else:
            dp[i] = arr[i]
    print(dp)
    print(max(dp))


numbers = input()
solution(numbers)
