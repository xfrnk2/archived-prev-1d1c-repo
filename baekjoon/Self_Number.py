#https://www.acmicpc.net/problem/4673

arr = set()
group = [i for i in range(1, 10000)]
for x in group:
    if 10000 < x:
        break
    temp = x
    x = list(str(x))
    #셀프넘버
    temp += eval("+".join(x))
    arr.add(temp)

for x in group:
    if x not in arr:
        print(x)
