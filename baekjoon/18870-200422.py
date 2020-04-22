#문제 : 18870번 좌표 압축
#주소 : https://www.acmicpc.net/problem/18870


input()
default_values = list(map(lambda x: int(x), input().split()))
set_list = sorted(set(default_values))
pair = {}

def put_pair(i, j):
    pair[j] = i

generate_result = [put_pair(index, value) for index, value in enumerate(set_list)]
print(' '.join([str(pair[x]) for x in default_values]))





