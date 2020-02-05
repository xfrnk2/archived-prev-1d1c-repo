#읽을거리 : https://stackoverflow.com/questions/14083111/should-i-use-encoding-declaration-in-python-3
#문제 : https://www.acmicpc.net/problem/11047
# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
# 둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)
#
# 출력
# 첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.
#
# 예제 입력 1
# 10 4200
# 1
# 5
# 10
# 50
# 100
# 500
# 1000
# 5000
# 10000
# 50000
# 예제 출력 1
# 6

# 예제 입력 2
# 10 4790
# 1
# 5
# 10
# 50
# 100
# 500
# 1000
# 5000
# 10000
# 50000
# 예제 출력 2
# 12



from typing import Sequence
from itertools import chain

def greedy(n: int, total_amount: int, values: Sequence[int]) -> int:
    coin_count = 0
    while 0 < total_amount:
        for value in reversed(values):
            if total_amount < value:
                continue
            q, r = divmod(total_amount, value)
            coin_count, total_amount = coin_count + q, r
    return coin_count


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr = list(chain(*arr))
    print(greedy(n, k, arr))
