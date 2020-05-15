
def origami_func(arr, x, y, n):



if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int,input().split())))

    origami_func(arr, 0, 0, n)