def func(n: str):
    if n == "":
        return ""
    print(n[0], end='')
    return func(n[1:])

func("hello")