m, n = map(int, input().split())

# min과 max를 바깥에서 사용했다가 좋지 못한 것 같아 아래와 같이 바꾸었다.
# 조심할 것 : 바깥 scope에서의 min과 max의 무분별적 사용// why? 조금 더 생각해서 for문 내부에서 더 효율적 코드를 짤 수 있기 때문

answer = 0
for _ in range(m):
    data = list(map(int, input().split()))
    min_value = min(data)
    answer = max(min_value, answer)

print(answer)