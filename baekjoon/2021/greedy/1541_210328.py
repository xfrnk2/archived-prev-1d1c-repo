#https://www.acmicpc.net/problem/1541
'''
소요시간 : 1시간
결과 : 런타임 에러
'''


def func(expression):
    if not expression[0].isdigit():
        return 0
    s = ''
    v = 0
    for i, j in enumerate(reversed(expression)):
        if j == '-':

            value = eval(s[::-1])
            value = -value
            value += v
            v = value
            s = ''
        else:
            s += j

    answer = eval(s[::-1]) + v
    return answer

print(func(input()))
# 위의 풀이가 런타임 에러가 나는 이유는?


'''
다른 정상적인 풀이
num = list(map(str,input().split("-")))

if "+" in num[0] :   # 첫번째 마이너스(-) 전에 플러스가 연속될 경우를 대비
    arr= list(map(int,num[0].split("+")))
    answer = sum(arr)
else : answer = int(num[0])  



for i in range(1,len(num)):  # 첫번째 마이너스(-) 이후부터는 전부 마이너스로 처리해야함.
    if "+" in num[i] :
        arr = list(map(int,num[i].split("+")))
        answer -= sum(arr)
    else : answer -= int(num[i])
    
print(answer)
'''