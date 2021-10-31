# 22:06 시작
# 소요시간 8분, 시간 초과 나옴.왜 그런걸까?
# 아, 이분탐색으로, 그러니까 start += 1//end -= 1해줄것이 아니라,
# start = mid + 1, end = mid - 1과 같은 형태로, 그리고 최종적으로
# 아래 코드에선 end를 반환하면 그것이 구하고자 하는 값이 된다.
# * 예전에 풀었던 코드를 잠깐 들여바도고 mid 기준으로 값을 더하거나 빼는 것을
# 적용시키고 end를 반환하는것도 다시금 확인하여 풀이를 성공시킴.
# 최종 소요시간 16분

def solution():
    N, M = map(int, input().split())
    tree = list(map(int, input().split()))
    tree.sort()

    start, end = tree[0], tree[-1]

    while start <= end:
        p = (start + end)//2
        acc = 0
        for i in range(N):
           if p < tree[i]:
               acc += tree[i] - p
        if acc < M: # 높이가 같거나 작은 경우 높이를 낮춰줌
            end = p - 1
        else:
            start = p + 1

    return end

print(solution())


