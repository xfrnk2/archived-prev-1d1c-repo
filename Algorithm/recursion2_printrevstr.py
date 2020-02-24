def func(n: str):
    if n == "":
        return
    func(n[1:])
    print(n[0], end='')
func("hello")
print("")
print("hello"[::-1])

