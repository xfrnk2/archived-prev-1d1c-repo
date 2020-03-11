#exception 상속을 이용한 마개조로 recursion depth 를 무시해버리는 형태로의 구현. 성능의 차이가 없다.
class Recurse(Exception):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


def recurse(*args, **kwargs):
    raise Recurse(*args, **kwargs)


def tail_recursive(f):
    def decorated(*args, **kwargs):
        while True:
            try:
                return f(*args, **kwargs)
            except Recurse as r:
                args = r.args
                kwargs = r.kwargs
                continue

    return decorated


@tail_recursive
def factorial(n, accumulator=1):
    if n == 0:
        return accumulator
    recurse(n-1, accumulator=accumulator*n)

print(factorial(5))


#일반적인 꼬리 재귀형태로의 구현
def general_tail_recursion(n, answer = 1):
    if n == 1:
        return answer
    return general_tail_recursion(n-1, answer * n)

print(general_tail_recursion(5))