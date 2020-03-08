#https://www.acmicpc.net/problem/11720
def function(num):
    return eval('+'.join(num))

if __name__ == '__main__':
   value = [int(input()) for _ in range(2)]
   print(function(str(value[1])))
