# https://www.acmicpc.net/problem/1365
'''
풀이를 보고 이해하여 문제 해결방법을 나름 정리후 손코딩.

1. 별도의 공간 필요 -> 최종적으로 전체 길이를 반환하기 위한 스택과 같은 배열 필요.
2. 별도의 공간을 순회하며 1에서 소개한 배열 내부의 특정 값과 비교
3. 2의 비교연산을 통해 배열내 원소에 변화를 주고, 최종적인 length를 반환

'''
from bisect import bisect_left
N = int(input())
line = list(map(int, input().split()))
dp = [line[0]]
for i in range(1, N):
    if dp[-1] < line[i]:
        dp.append(line[i])
    else:
        dp[bisect_left(dp, line[i])] = line[i]
print(N - len(dp))
