# https://www.acmicpc.net/problem/12015
# C번 문제와 같지만, 입력 데이터의 범위가 더 늘어났다.
# 풀이 방법이 생각이 안나 검색후 이해하였고, 코드를 돌리며 확인했다.
# 나중에 다시 풀어볼 것이다.
# 여담이지만 이제는 한 문제를 가지고 깊이 고민하기보다는, 5~10분 안에
# 명쾌한 답이 생각이 나지 않는다면 풀이를 보고 이해후 빠르게 넘어가는게
# 좋겠다는 판단이 들고 있다. 많은 문제를 접해보고 내 것으로 만드는 것이
# 더 중요할 것이고 효율적일것이란 생각이 들었기 때문이다.

from bisect import bisect_left #이진탐색 코드, 같은 수일 경우 왼쪽 index를 돌려준다

input()
A = list(map(int, input().split()))
dp = []

for i in A:
    k = bisect_left(dp, i) #자신이 들어갈 위치 k
    if len(dp) <= k: #i가 가장 큰 숫자라면
        dp.append(i)
    else:
        dp[k] = i #자신보다 큰 수 중 최솟값과 대체

print(len(dp))


'''
그러나 만약 다음과 같은 수열이 주어지면

A = 3 5 7 9 2 1 4 8

우리가 예상하는 dp는 3 5 7 9 이지만

실제 dp는 1 4 7 8로 나온다.

따라서 해당 알고리즘은 정답 수열을 도출해내는 데에는 사용할 수 없다.

 

# 풀 수 없는 문제

가장 긴 증가장 긴 증가하는 부분 수열 4

https://www.acmicpc.net/problem/14002

가장 긴 증가장 긴 증가하는 부분 수열 5

https://www.acmicpc.net/problem/14003
'''