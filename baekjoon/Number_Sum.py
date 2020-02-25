#https://www.acmicpc.net/problem/11720
def func(n, num):
    if n <= 0:
        return 0
    return int(str(num)[n-1]) + func(n - 1, num)

def func2(num):
    return eval('+'.join(num))

if __name__ == '__main__':
   value = [int(input()) for _ in range(2)]
   print(func(value[0], value[1]))
   print(func2(str(value[1])))
