def func(number, value, value_count):
    value = value % 10 * 10 + (value // 10 + value % 10) % 10
    if number == value :
        return value_count
    return func(number, value, value_count + 1)

if __name__ == "__main__":

    number = int(input())
    if number < 10:
        number *= 10

    print(func(number, number, 1))