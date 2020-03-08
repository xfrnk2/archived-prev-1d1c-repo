#https://www.acmicpc.net/problem/1110

# def func(number, value, value_count):
#     value_count += 1
#     value = value % 10 * 10 + (value // 10 + value % 10) % 10
#     if value == number:
#         return value_count
#     return func(number, value, value_count)
#
# if __name__ == "__main__":
#     num = int(input())
#
#     assert 0 <= num <= 99
#
#     if num < 10:
#         num *= 10
#
#     print(func(num, num, 0))

def func(value: int) -> int:
    number , count = value, 0

    while True:
        if value == 0:
            break
        if not 0 <= value <= 99:
            break

        value, count = value % 10 * 10 + (value // 10 + value % 10) % 10, count + 1
        if value == number:
            break
    return count

if __name__ == "__main__":
    num = int(input())
    print(func(num))
