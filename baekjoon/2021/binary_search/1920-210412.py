# https://www.acmicpc.net/problem/1920
input()
arr1 = input().split()
input()

print(' '.join(['1' if x in arr1 else '0' for x in input().split()]))