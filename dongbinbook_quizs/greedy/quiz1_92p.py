from collections import Counter
N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

# 염두할 것 : 더 좋은 풀이방법이 있는지 한번 더 고민해보자.
# 1회차 풀이

# group = Counter(arr)
# so_group = sorted(group, reverse=True)
# max_value = max(group)
# print(so_group)
#
# if 2 <= group[max_value]:
#     for _ in range(M):
#         print(max_value, end='')
# else:
#     answer = []
#     a = 0
#     for i in range(1, M + 1):
#         if a < K:
#             answer.append(so_group[0])
#             a += 1
#         else:
#             answer.append(so_group[1])
#             a = 0
#     print(f'{answer} ', end='')

# 2회차 풀이
# group = sorted(arr)
# first, second = group[N-1], group[N-2]
# result = 0
#
# for i in range(M):
#     m, n = divmod(i, 3)
#     if 0 < m and n == 0:
#         result += second
#     else:
#         result += first
#
# print(result) # 성공

# 교재 내 답안 예시
arr.sort()
first, second = arr[N-1], arr[N-2]

count = int(M/(K+1)) * K
count += M % (K+1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (M-count) * second # 두 번째로 큰 수 더하기

print(result)

#input
# 5 8 3
# 2 4 5 4 6
#output
#46

#itput
# 5 7 2
# 3 4 3 4 3

#output
# 28