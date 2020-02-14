#https://www.acmicpc.net/status?user_id=xfrnk2&problem_id=2562&from_mine=1

arr = [int(input()) for _ in range(9)]

index, number = 0, 0
for i, j in enumerate(arr):
    if number < j:
        index, number = i, j

print(number)
print(index+1)