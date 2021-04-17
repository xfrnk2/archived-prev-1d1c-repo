from collections import Counter
N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

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
group = sorted(arr)
first, second = group[N-1], group[N-2]
result = 0
#두번째 풀이

for i in range(M):
    m, n = divmod(i, 3)
    if 0 < m and n == 0:
        result += second
    else:
        result += first

print(result) # 성공