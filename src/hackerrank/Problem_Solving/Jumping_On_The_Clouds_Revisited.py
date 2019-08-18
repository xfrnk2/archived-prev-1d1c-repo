#https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
#Jumping_On_The_Clouds:Revisited

def jumping_on_clouds(c, k):
    n = 0
    num = 100

    times = len(c) // k

    if c[0] == 0:
        num -= 1
    else:
        num -= 3

    for _ in range(times):

        n += k
        if n == len(c):
            break
        if c[n] == 1:
            num -= 3
        else:
            num -= 1

    return num

