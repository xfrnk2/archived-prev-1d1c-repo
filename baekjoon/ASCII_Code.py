#https://www.acmicpc.net/problem/11654
def func(value):
    if not value:
        return value
    assert len(value) < 2, 'The length is not proper'
    return ord(value)
if __name__ == '__main__':
    value = input()
    print(func(value))