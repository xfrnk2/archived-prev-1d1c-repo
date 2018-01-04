# coding=utf-8

"""
숫자를 입력 받아 화면에 아래와 같이 출력합니다.
숫자의 출력 범위는 x를 입력 받아 x^2(x의 제곱수) 만큼 출력합니다.

즉 5를 입력 받아 1~25까지 출력합니다.

25 24 23 22 21
10  9  8  7 20
11  2  1  6 19
12  3  4  5 18
13 14 15 16 17

이와 같이 숫자가 회오리 치듯이 출력 되어야 합니다.





4를 입력 받으면 아래와 같이 출력합니다.

16 15 14 13
 5  4  3 12
 6  1  2 11
 7  8  9 10



반대 방향으로도 출력해 봅니다.

25 10 11 12 13
24  9  2  3 14
23  8  1  4 15
22  7  6  5 16
21 20 19 18 17


16  5  6  7
15  4  1  8
14  3  2  9
13 12 11 10

몫을 구할때 //, 나머지를 구할때 %

for, list() 등의 기능을 적극 활용합니다.



x = 4
array = [ [ 0 ] * x for _ in range( x ) ]


# array = range(1,x*x)
# for _ in range(1, x+1):

# position =
def set_value_in_position( x, y, value ):
    # array[ y * 3 + x ] = value
    array[ x ][ y ] = value


# set_value_in_position(1,1,10)


# 수평 방향으로 -1
set_value_in_position(1,0,v[1])
# 수직 방향으로 +1
set_value_in_position(2,0,v[2])
# 수평 방향으로 +2
set_value_in_position(2,1,v[3])
set_value_in_position(2,2,v[4])
# 수직 방향으로 -2
set_value_in_position(1,2,v[5])
set_value_in_position(0,2,v[6])
# 수평 방향으로 -3
set_value_in_position(0,1,v[7])
set_value_in_position(0,0,v[8])

a[1][1]=1
# 수평 방향으로 -1
a[1][0]=2
# 수직 방향으로 +1
a[2][0]=3
# 수평 방향으로 +2
a[2][1]=4
a[2][2]=5
# 수직 방향으로 -2
a[1][2]=6
a[0][2]=7
# 수평 방향으로 -3
a[0][1]=8
a[0][0]=9


for j in range( 0, x ):
    print( array[ j ] )


size = 5
array = ['' for _ in range(25,0,-1)]


def printfield() -> None:
    for array in [["*" for _ in range(size)] for _ in range(size)]:
        for block in array:
            print(block, end='')
        print('')

    print()


print(array[1])


# set_value_in_position(1,1,10)


def printfield(size):
    for array in [["*" for _ in range(size)] for _ in range(size)]:
        for block in array:
            print(block, end='')
        print('')

    print()




print(printfield(size))



print(numbers())


# position =

while True:
    size = int(input("출력할 크기는? :"))
    if size == 0 :
        print("good bye~")
        break
    if size<3 or size>9:
        print("3에서 9 사이만 인정")
        continue

    a = [[0]*size for _ in range(size)]
    start = (size-1)//2
    c = -1
    h = start
    v = start
    n = 0
    n = n + 1
    a[v][h]=n
    for i in range(1, size + 1 ):
        c = c * (-1)

        for _ in range(0,i):
            h = h+1*c
            if size**2==n:

                break
            n = n+1
            a[v][h]= n
        for _ in range(0,i):
            v=v+1*c
            if size**2==n:
                break
            n=n+1
            a[v][h]=n
    print("")
    for j in range(0, size):

        print(a[j])


"""

#1~25까지의 숫자를 그룹을 만들거나 정해진 규칙으로 나타나게 한다.



while True:
    size = int(input("출력할 크기는? :"))
    if size == 0 :
        print("good bye~")
        break
    if size<3 or size>9:
        print("3에서 9 사이만 인정")
        continue

    a = [[0]*size for _ in range(size)]
    start = (size-1)//2
    c = -1
    h = start
    v = start
    n = 0
    n = n + 1
    a[v][h]=n
    for i in range(1, size + 1 ):
        c = c * (-1)

        for _ in range(0,i):
            h = h+1*c
            if size**2==n:

                break
            n = n+1
            a[v][h]= n
        for _ in range(0,i):
            v=v+1*c
            if size**2==n:
                break
            n=n+1
            a[v][h]=n
    print("")
    for j in range(0, size):

        print(a[j])

