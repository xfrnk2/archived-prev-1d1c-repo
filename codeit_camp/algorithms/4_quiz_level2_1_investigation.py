# 사실 정답 코드와 같은 내용이다. 해설을 보고 이해했는데, 그 전에는 어떻게든 O(n log n)의 시간복잡도를 가지는
# 코드를 짤 수 없었다. level1의 bruthforce와 같은 요구조건의 문제인데, O(n^2)의 시간복잡도를
# O(n log n)로 개선하라는 문제이다.

def max_corss(profits, start, end):
    mid = (start + end) // 2
    left_sum, right_sum = 0, 0
    left_max, right_max = profits[mid], profits[mid + 1]

    for i in range(mid, start - 1, -1):
        left_sum += profits[i]
        left_max = max(left_max, left_sum)

    for j in range(mid + 1, end + 1):
        right_sum += profits[j]
        right_max = max(right_max, right_sum)

    return left_max + right_max


def sublist_max(profits, start, end):
    if start == end:
        return profits[start]

    pivot = (start + end) // 2

    a = sublist_max(profits, start, pivot)
    b = sublist_max(profits, pivot + 1, end)
    c = max_corss(profits, start, end)
    # ab = sublist_max(profits, start, end)
    return max(a, b, c)


# 테스트
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max(list2, 0, len(list2) - 1))

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max(list3, 0, len(list3) - 1))

list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
print(sublist_max(list4, 0, len(list4) - 1))