# coding=utf-8

"""
화면에 아래와 같이 출력합니다.

*
**
***
****
*****

*****
****
***
**
*


    *
   **
  ***
 ****
*****

*****
 ****
  ***
   **
    *


단 아래와 같은 방법으로 출력하지 않습니다.

print( '*' );
print( '**' );
print( '***' );
print( '****' );
print( '*****' );


for, list() 등의 기능을 적극 활용합니다.

"""

# TODO - 주석 작성해주세요. - 12번 이슈를 확인합니다.
#         https://github.com/xfrnk2/puyopuyo/issues/11
#         https://github.com/xfrnk2/puyopuyo/issues/12

stone = "*"
block = " "

# TODO - 사용하지 않는 변수는 _ 로 무시할 수 있습니다(권장사항)
#        https://github.com/xfrnk2/puyopuyo/issues/15
stones = [ "*" for _ in range( 6 ) ]


# TODO - 명명 규칙을 일관성 있게 해주세요. 어느 것은 카멜 표기법, 어느 것은 언더스코어...
# TODO - 사실 print_right, print_left, printField 등의 함수명을 보면 무슨 일을 하는 함수인지 잘 모르겠어요.
def print_right( x ):
    stones[ x ] = stone
    stones[ x - 1 ] = block
    fields = ''.join( stones[ 1:6 ] )
    print( fields )


field1 = [ "" for _ in range( 6 ) ]


def print_left( x ):
    field1[ x ] = block
    field1[ x - 1 ] = stone
    fields = ''.join( field1 )
    print( fields )


# TODO - [ ] 는 선행평가, ( ) 는 지연평가. 이런 경우는 지연 평가가 좋습니다.
# TODO - list 는 파이썬 자체 내장(빌트인) 예약어이므로 변수명으로 사용하지 않는게 좋습니다.
list = [ 1, 2, 3, 4, 5 ]
list1 = [ 5, 4, 3, 2, 1 ]

# TODO = 굳이 리스트를 만들어서 for 돌리지 않고 range(1, 6) 이렇게 쓰는 쪽이 좋겠죠?
for x in list:
    print_left( x )
print( "    " )
for x in list1:
    print_left( x )
print( "    " )
for x in list:
    print_right( x )
print( "    " )
for x in list:
    print_right( -x )
print( "    " )

print( "----------*----------*----------*----------\n" )

# TODO - 힌트를 드립니다.
star = '*'
whitespace = ' '


def solve_1st() -> None:
    """
    1번째 문제를 풉니다.
        """
    for x in range( 5, 0, -1 ):
        output = ''
        for y in range( 6, 1, -1 ):
            if x < y:
                output += star
            else:
                output += whitespace
        print( output )

solve_1st()
print('\n')

def solve_2th() -> None:
    """
    2번째 문제를 풉니다.
    """
    for x in range( 5, 0, -1 ):

        output = ''

        for y in range( 5 ):
            if x > y:
                output += star
            else:
                output += whitespace

        print( output )


solve_2th()
print( '\n' )

def solve_3rd() -> None:
    """
    3번째 문제를 풉니다.
    """
    for x in range( 5, 0, -1 ):

        output = ''

        for y in range( 5, 0, -1 ):
            if x < y:
                output += whitespace

            else:
                output += star

        print( output )

solve_3rd()
print( '\n' )

def solve_4th() -> None:
    """
    4번째 문제를 풉니다.
    """
    for x in range( 5, 0, -1 ):

        output = ''

        for y in range( 1, 6 ):
            if x <= y:
                output += star
            else:
                output += whitespace

        print( output )


solve_4th()
