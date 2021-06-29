def trapping_rain(buildings):
    count = 0

    for i in range(0, max(buildings)):
        for j in range(1, len(buildings)-1):
            if buildings[j] == i:
                if i < max(buildings[:j]) and i < max(buildings[j:]):
                    count += 1
                    buildings[j] += 1
    return count

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))