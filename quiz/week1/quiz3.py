# coding=utf-8

"""
아래의 함수를 디버깅 해서 step into 기능을 통해 흐름을 파악해 봅니다.
아래의 흐름이 어떻게 이루어지는지 설명할 수 있어야 합니다.

"""


def fibonacci(n: int):
    assert n >= 0, "Invalid argument, must n >= 0"
    escape_condition = (n is 0) or (n is 1)

    if escape_condition:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


"""
아래의 함수는 잘못 된 부분이 있습니다.
적절히 수정해 봅시다.
"""


def factorial(n: int):
    if n == 0:
        return 0

    assert n > 0, "Invalid argument, must n > 0"

    escape_condition = (n == 1)
    if escape_condition is True:
        return 1

    return n * factorial(n - 1)


if __name__ == '__main__':
    x = 10
    result = fibonacci(x)
    print(result)

    x = 5
    result = factorial(x)
    print(result)
