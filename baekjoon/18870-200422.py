#문제 : 18870번 좌표 압축
#주소 : https://www.acmicpc.net/problem/18870


input()
default_values = list(map(int, input().split()))
set_list = sorted(set(default_values))
pair = {}

for index, value in enumerate(set_list):
    pair[value] = index

print(' '.join([str(pair[x]) for x in default_values]))





