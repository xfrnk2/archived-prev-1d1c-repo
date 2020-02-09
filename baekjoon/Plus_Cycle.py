#https://www.acmicpc.net/problem/1110
number = int(input())
if number < 10:
    number *= 10
value = number
value_count = 0
while True:
    value = value%10*10 + (value//10+value%10)%10
    value_count += 1
    if value == number:
        break
print(value_count)







