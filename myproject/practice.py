x = 2
y = 3
z = 4
def func1(x):
    print("x")
def func2(x):
    print("x")
    func1(x)
    func3(x)
def func3(x):
    print("x")
if func1(x) or func2(y) or func3(z):
    pass

vv = []
def func5(x, y):
    vv.append((x, y))
    print(vv)
    if (x, y) in vv:
        print("ddd")

func5(1,2)