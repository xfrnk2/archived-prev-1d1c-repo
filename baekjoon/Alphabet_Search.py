#https://www.acmicpc.net/problem/10809
from string import ascii_lowercase
def func(value):
    length = len(ascii_lowercase)
    result = ['-1' for _ in range(length)]
    for i, j in enumerate(ascii_lowercase):
        try:
            b = value.index(j)
        except ValueError:
            continue
        result[i] = str(b)
    return ' '.join(result)

if __name__ == '__main__':
    s = input()
    print(func(s))
