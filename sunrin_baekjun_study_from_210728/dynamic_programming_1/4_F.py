# https://www.acmicpc.net/problem/1912
# 첫 번째 풀이. 방법이 생각이 안나서 다른사람의 코드를 보고 이해했다. 그리고
# 흐름을 기억해서 코딩해보고, 그 다음 내 방식으로 수정을 했다.
n = int(input())
arr = list(map(int, input().split()))
sum_arr = [arr[0]]

for i in range(n-1):
    sum_arr.append(max(sum_arr[i] + arr[i+1], arr[i+1]))
print(max(sum_arr))