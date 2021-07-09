def min_fee(pages_to_print):
    pages_to_print.sort()
    ans = 0
    for i, j in enumerate(pages_to_print):
        ans += j * (len(pages_to_print) - i)
    return ans

# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
