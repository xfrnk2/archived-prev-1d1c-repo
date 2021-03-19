N, S = list(map(int, input().split()))
D = list(map(int, input().split()))
print(N, S, D)
result = 0
i, temp = 0, 0

def func(i, temp):
    global result

    if i == N:
        return
    if temp + D[i] == S:
        result += 1


    func(i+1, temp)
    func(i+1, temp+D[i])

func(0, 0)
print(result)