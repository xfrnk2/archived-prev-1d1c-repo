# 진법 변환을 함수로 구현해본다.

def dec_to_bin(decimal):
    a = ''
    while decimal > 1:
        decimal, n = divmod(decimal, 2)
        a = str(n) + a
    a = str(decimal) + a
    return a

def dec_to_hex(decimal):
    num = ['A', 'B', 'C', 'D', 'E', 'F']
    a = ''
    while decimal > 1:
        decimal, n = divmod(decimal, 16)
        if 10 <= n:
            a = num[n - 10] + a
        else:
            a = str(n) + a
    a = str(decimal) + a
    return a

def dec_to_oct(decimal):
    a = ''
    while decimal > 1:
        decimal, n = divmod(decimal, 8)
        a = str(n) + a
    a = str(decimal) + a
    return a


def bin_to_dec(binary: str):
    v = 0
    a = 0
    for i in range(len(binary)-1, -1, -1):
        if binary[i] == '1':
            a += 2 ** v
        v+= 1
    return a


print(dec_to_bin(22))
print(dec_to_oct(22))
print(dec_to_hex(22))
print(bin_to_dec('10110'))

