'''
20/05/23 파이썬 단톡방 파린이님 曰
n,m = 10,10
d = [[0]* m for _ in range(n)]
f = [[ 0 ] * m] * n

d[0][1] = 1로 바꾸면 d[0][1]만 바뀌지만
f[0][1] = 1로 바꾸면 지정된 행 부분 전체가 모두 1로 바뀐다.

f[0][1] = 1 의 경우는 처음 접하다보니 기묘하다.
게다가 bool(d==f)의 결과는 True이다.
어째서일까?

for와 multiply(*) 사이에 아직 알지못하는 사실이 숨어 있는 걸까?
관련된 stackoverflow 글을 찾았다.!
https://stackoverflow.com/questions/240178/list-of-lists-changes-reflected-across-sublists-unexpectedly
'''