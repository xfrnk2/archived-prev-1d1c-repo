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



stone = "*"
block = " "
field = [ " " for x in range( 6 ) ]


def printField( x ):
    field[ x ] = stone
    field[ x - 1 ] = block
    fields = ''.join( field )
    print(fields)


list = [5, 4, 3, 2, 1]
for x in list:
    printField(x)
print("    ")
for x in list:
    printField(-x)
print("    ")