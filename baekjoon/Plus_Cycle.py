#https://www.acmicpc.net/problem/1110

def func(number, value, value_count):
    value_count += 1
    value = value % 10 * 10 + (value // 10 + value % 10) % 10
    if value == number:
        return value_count
    return func(number, value, value_count)

if __name__ == "__main__":
    num = int(input())
    if num < 10:
        num *= 10
    print(func(num, num, 0))