def fiboTail(n):
    return FiboTailRec(n, 0, 1)

def FiboTailRec(n, before, next):
    if n == 0:
        return before
    else:
        return FiboTailRec(n-1, next, before + next)

print(fiboTail(8))

def fiboTail2(n):
    return fibo(n, 0, 1)
def fibo(n, left, right):
    if 0 == n:
        return 0
    elif n == 1:
        return right
    else:
        return fibo(n-1, right, right+left)

print(fiboTail2(8))