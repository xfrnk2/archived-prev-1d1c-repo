def func(n: str):
    if n == "":
        return 0
    return 1 + func(n[1:])
print(func("hello there"))