# 높이 n개의 계단을 올라가는 방법을 리턴한다
def staircase(stairs, possible_steps):
    d = [0] * (stairs + 1)
    d[0], d[1] = 1, 1
    for height in range(2, stairs + 1):
        for step in possible_steps:
            if height - step >= 0:
                d[height] += d[height - step]

    return d[stairs]


print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))