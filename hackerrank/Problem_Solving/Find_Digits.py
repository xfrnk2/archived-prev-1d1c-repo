#https://www.hackerrank.com/challenges/find-digits/problem

def findDigits(n:int) -> int:
    if n == 0:
        return n

    count = 0
    for x in str(n):
        if x == '0':
            continue
        if n % int(x) == 0:
            count += 1
    return count