# https://www.hackerrank.com/challenges/ctci-merge-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
def countInversions(n, arr):
    count = 0
    for x in range(1, n):
        while 0 < x and arr[x] < arr[x-1]:
            arr[x], arr[x-1] = arr[x-1], arr[x]
            count, x = count + 1, x - 1
    return count