#https://www.hackerrank.com/challenges/find-digits/problem

def findDigits(n: int) -> int:
    if n == 1:
        return n

    l = len(str(n))
    count = 0

    for x in range(1, l + 1):
        num = int((n % 10 ** x) / 10 ** (x - 1))
        if num == 0:
            continue
        if n % num == 0:
            count += 1

    return count