from functools import reduce


def binaryToDecimal(num):
    res = 0
    for i,j in enumerate(num[::-1]):
        res += int(j)*(2**i)
    print(res)

binaryToDecimal('11011010010')

def binaryToOctal(num):

    result = ''
    temp = ''
    for i, j in enumerate(num[::-1]):
       if j == '1':
            temp += str(2 **(i%3))

       if (i+1) % 3 == 0 or i == len(num)-1:
            result += str(reduce(lambda x, y: int(x) + int(y), temp))
            temp = ''
    return int(result[::-1])

print(binaryToOctal('11011010010'))
