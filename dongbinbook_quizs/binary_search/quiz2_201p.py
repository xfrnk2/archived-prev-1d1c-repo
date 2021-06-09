# 12:31
import sys
import timeit
'''
input
4 6
19 15 10 17

output
15
'''
start_time = timeit.default_timer()
r_input = sys.stdin.readline
n, m = map(int, r_input().split())
arr = list(map(int, r_input().split()))
answer = 0
start, end = 0, max(arr)
while start <= end:
    total = 0
    mid = (start + end)//2
    for x in arr:
        if mid < x:
            total += (x - mid)
    if total < m:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1
print(answer)

#1차 : 0.5912864





'''
1. 제일 큰 수 - 제일 작은 수 // 2 를 기준값으로 잡는다.
2. 기준값일때 m을 만족하면 종료
   자른결과가 m보다 작으면 start=그대로, end=기준값
   반대는 start=기준값, end=그대로
'''
    











end_time = timeit.default_timer()

print(f'걸린 시간 : {end_time - start_time}')