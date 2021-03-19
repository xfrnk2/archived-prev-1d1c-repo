#https://www.acmicpc.net/problem/2839
#5와 3의 규격이 있고, 5와 3만으로 등분할 수 없을 시 -1을 반환.

def func(n):

    a = n // 5
    if n < 5:
        a = 0

    for x in range(a, -1, -1): # 3, 2, 1
        b = n - (5 * x) # 나머지만을 구할때
        if b % 3 == 0:
            return x + b // 3
    return -1

queue = [18, 4, 6, 9, 11]
for x in queue:
    print(func(x))

#풀이 결과 : 성공
#소요 시간 : 30분

