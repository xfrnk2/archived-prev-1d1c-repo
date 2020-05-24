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

파린이님 :
일단 제가 해본방법으로는 id를 찍어서 각각을 확인해보니 f=[[0]*3]*3 으로 만들었을때 각 행끼리 주소값이 같은것을 확인했습니다.
d = [[0]*3 for _ in range(3)] 으로했을때는 각각원소들이 다른 주소값을 가지고 있구요.

근데 신기한건 f[0][1] , f[0][0] 들은 다른 주소값을 가지고있는데 id로 찍었을때 shallow copy가 된거같은데 신기하네요 ㅋㅋ...

,
아... 서치해보다보니,
list로 만들면 주소값들을 공유하지만 각각원소끼리는 주소값을 공유하지 않는것같습니다.
[[0]*3] *3 으로 만들게되면 하나의 리스트 안에서 주소를 공유해서 새로운 리스트를 만드는게 아니라 하나의 리스트에서 추가해서 만들어서 그런것같구요
[[0]*3 for _ in range(3)] 으로 만들게 되면, for문이 돌때마다 새로운 리스트에 계속 만들게 되서 각각 원소들이 주소공유를 하지 않는것같습니다.
결국 리스트안에 원소들의 int값들이 다른 주소값들을 가지고 있는거였네요.

생성자와 같은 역할을 하는 id가 만들어지는것의 차이
d-> [0]*3이 호출될 때마다 다른 id가 부여됨
f-> [0]*3이 호출될때 부여된 id가 계속해서 늘어남, 같은 주소를 가리키고 있음


즉
f = [[ 0 ] * m] * n
[[0]*m]을 n번 참조하고 있는 것이다. n개의 복사본 들이 아니라.
-> Creates a list that references the internal [1,1,1,1] 3 times - not three copies of the inner list,
 so any time you modify the list (in any position), you'll see the change three times.
> inner = [1,1,1,1]
> outer = [inner]*3
> outer
[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
> inner[0] = 5
> outer
[[5, 1, 1, 1], [5, 1, 1, 1], [5, 1, 1, 1]]

'''
n,m = 10,10
d = [[0]* m for _ in range(n)]
f = [[ 0 ] * m] * n
for x in f:
    print(id(x))
for y in d:
    print(id(y))
print('====')
f[0][1] = 1
print([id(x) for x in f[0]])