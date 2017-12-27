from time import sleep
# time의 sleep을 불러옵니다
import os

# print("■■■■■■■")
# print("■□□□□□■")
# print("■□□□□□■")
# print("■□□□□□■")
# print("■□□□□□■")
# print("■□□□□□■")
# print("■■■■■■■")
#
# print("■■■■■■■")
# for x in range(5):
#     print("■□□□□□■")
# print("■■■■■■■")

stone = "●"
block = "□"
field = [ "□" for x in range( 7 ) ]

# x = 6
# field[ x ] = stone
#
# # 지금은 문자를 문자열이라고 생각해도 된다.
# # join은 문자열에 이터레이터(반복가능한 녀석)를 합쳐버리는 기능을 하는 함수다
# fields = ''.join( field )
# clear()
# print(fields )

def clear():
    """
    주석을 달아봅니다. cls을 통해 출력화면을 백지상태로 만듭니다
    """
    os.system('cls')


def printField( x ):
    sleep( 1 )
    field[ x ] = stone
    field[ x + 1 ] = block
    fields = ''.join( field )
    clear()
    print(fields )

i = 6
printField( i - 1 )
printField( i - 2 )
printField( i - 3 )
printField( i - 4 )