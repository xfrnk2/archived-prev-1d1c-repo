def HowType(l:list):
    if len(l) != 2:
        return False
    for x in l:
        if 0 < int(x) <= 1000:
            return True
        else:
            return False


def testing(ex):
    ex = ex.split(' ')

    if not HowType(ex):
        print("요구조건에 맞지 않게 입력했습니다")
        exit()

    m, n = int(ex[0]), int(ex[1])

    for i in range(n):
        for j in range(m):
            print('*', end='')
        print('')

ex = input()
testing(ex)