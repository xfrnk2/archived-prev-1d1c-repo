# def binaryToDecimal(num):
#     value = num
#     pivot = len(value[::4])
#
#     _value = value[::-1]
#     result = []
#     group = [(4*x-4, 4*x) for x in range(1, pivot+1)]
#     c = ''
#     for i in range(pivot):
#         x, y = group[i]
#         result.append(_value[x:y])
#
#     for y in result:
#         r = 0
#         for i, j in enumerate(y):
#            r += int(j)*(2**i)
#         c += str(r)
#
#     print(result)
#     print(c)
# binaryToDecimal('11011010010')
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

