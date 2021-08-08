# https://www.acmicpc.net/problem/2805

'''
4 7
20 15 10 17
'''

N, M = map(int, input().split())
tree = list(map(int, input().split()))
tree = sorted(tree)


start, end = 1, tree[-1] # start는 나무 길이 최소가 1이므로. 시작을 tree[0]로 하면 틀린 코드다.
while start <= end:
    mid = (start + end) // 2
    count = 0
    for t in tree:

        if mid < t:
            count += t - mid
    if M <= count:
        start = mid + 1

    elif M > count:
        end = mid - 1


print(end)
