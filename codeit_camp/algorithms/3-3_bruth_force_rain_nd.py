# 주어진 테스트케이스 2개는 만족할지언정 올바른 풀이법이 아닌 것 같다. 무효 처리할 풀이.


def trapping_rain(buildings):
    count = 0
    highest = max(buildings)
    for i in range(1, highest+ 1):
        for j in range(len(buildings)):
            if j < i:
                count += 1

    return count

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))