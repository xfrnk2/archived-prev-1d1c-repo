#https://www.acmicpc.net/problem/4344
from functools import reduce

number = int(input())
scores = [list(map(int, input().split())) for _ in range(number)]
for score in scores:
    average = reduce(lambda a,b : a + b, score[1:]) / score[0]
    values = list(filter(lambda x, : average < x, score[1:]))
    print( "%0.3f" % round(float(len(values)/(len(score)-1)) * 100, 3) + "%")

