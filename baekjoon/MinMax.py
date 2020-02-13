#https://www.acmicpc.net/submit/10818/17664185

n = int(input())
numbers = list(map(int, input().split()))

min_value = max_value = numbers[0]
for x in numbers:
    if x < min_value:
        min_value = x
    if max_value < x:
        max_value = x

print(str(min_value) + " " + str(max_value))