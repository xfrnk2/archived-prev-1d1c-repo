def countInversions(arr):
    length = len(arr)
    flag = False
    mid = length//2
    if length % 2 == 1:
        flag = True
        mid += 1

    a = arr[:mid]
    b = arr[mid:]
    if not 1 == len(b):
        countInversions(a)
        countInversions(b)
    else:
        if flag:
            for x in a:
                if x > b[0]:
                    print("??")
                    print(x, b[0])
    return 0