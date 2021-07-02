def consecutive_sum(start, end):
    mid = (start + end) // 2
    if start == end:
        return start
    return consecutive_sum(start, mid) + consecutive_sum(mid+1, end)

# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))