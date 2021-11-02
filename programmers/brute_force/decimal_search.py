from itertools import permutations

# 배울 수 있었던 것 : 조합을 구하는 방법과 처리 (여러번을 해도 숙달되지 않은 상황이다. 다시 보면 기억이 안난다..)
# 소수 구하는 방법 알고리즘 : 루트(N)까지 탐색하면 구할 수 있고, O(log n)의 시간복잡도를 가진다.
# ( 참고 한 곳 : https://myjamong.tistory.com/139 )
# 위에 덧붙이자면, '에라토스테네스의 체'라는 소수 구하기 알고리즘이 있다고 한다. 잘 모르겠지만. 성능차이가 큰가보다.
# 이정도 수준은 현재로선 그냥 넘어가기로 한다.
def solution(numbers):
    ans = 0
    container = []
    for i in range(1, len(numbers) + 1):
        dp = ((permutations(numbers, i)))
        for d in dp:
            container.append(int(''.join(d)))
    container = set(container)

    def check(n):

        if n <= 1:
            return True

        t = 2
        t2 = n ** 0.5
        while t <= t2:
            if n % t == 0:
                return True
            t += 1
        return False

    for n in container:
        if not check(n):
            ans += 1
    return ans
