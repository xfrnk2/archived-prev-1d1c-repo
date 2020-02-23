def func(n):
    if n < 2:
        print(n)
    else:
        func(n//2)
        print(n%2)
    
print(func(2))