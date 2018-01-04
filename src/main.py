from time import sleep
# time 모듈의 sleep 함수를 불러옵니다
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
field = ["□" for x in range(7)]


# x = 6
# field[ x ] = stone
#
# # 지금은 문자를 문자열이라고 생각해도 된다.
# # join 함수는 이터레이터(반복가능한 객체)를 합쳐서 문자열로 만든다.
# fields = ''.join( field )
# clear()
# print(fields )

def clear():
    """
    주석을 달아봅니다. cls 명령어를 실행해 출력화면을 백지 상태로 만듭니다
    """
    os.system('cls')


def print_field(x):
    sleep(1)
    field[x] = stone
    field[x + 1] = block
    fields = ''.join(field)
    clear()
    print(fields)


i = 6
print_field(i - 1)
print_field(i - 2)
print_field(i - 3)
print_field(i - 4)
