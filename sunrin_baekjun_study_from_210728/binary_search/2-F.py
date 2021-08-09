# https://www.acmicpc.net/problem/1477
'''
6 7 800
622 411 201 555 755 82
'''
# 틀린 풀이이다. 끼워 맞춰가기 식 생각의 흐름대로 그냥 작성했다.
# N, M, d = map(int, input().split())
# l = sorted(list(map(int, input().split())))
# print(l)
# d_d = [l[i+1] - l[i] for i in range(N-1)] + [d - l[-1]]
#
# print(d_d)
#
# if N >= M:
#     if max(d_d) % 2 == 1:
#         print(max(d_d) // 2) + 1
#     else:
#         print(max(d_d) // 2)
# else:
#     print(max(d_d) // ((M-N)+2))


# 2차 풀이, 다른 사람 풀이 보고 이해하고 푼 것.
#
# N, M, L = map(int, input().split())
# l = list(map(int, input().split()))
# l.append(0)
# l.append(L - 1)
# l.sort()
# start, end = 0, L - 1
#
# while start <= end:
#     mid = (start + end) // 2
#     count = 0
#     for i in range(1, len(l)):
#         v = l[i] - l[i - 1]
#         if mid < v:
#             count += (v - 1) // mid
#     if count > M:
#         start = mid + 1
#     else:
#         ans = mid
#         end = mid - 1
#
# print(ans)



# 3차 풀이. 2차 풀이와 별 크게 다르진 않다.
#
N, M, L = map(int, input().split())
l = sorted(list(map(int, input().split())))

start, end = 0, L - 1
distance = [l[0]] + [l[i+1] - l[i] for i in range(len(l)-1)] + [end-l[-1]]


while start <= end:
    mid = (start + end) // 2
    count = 0
    for d in distance:
        if mid < d:
            count += (d - 1) // mid
    if count > M:
        start = mid + 1
    else:
        end = mid - 1
        ans = mid
print(ans)