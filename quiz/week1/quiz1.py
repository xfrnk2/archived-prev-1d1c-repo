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
field = [ "*" for x in range( 6 ) ]

def printField( x ):
    field[ x ] = stone
    field[ x - 1 ] = block
    fields = ''.join( field[1:6])
    print(fields)

field1 = [ "" for x in range( 6 ) ]
def printleft( x ):
    field1[x] = block
    field1[x - 1] = stone
    fields = ''.join(field1)
    print(fields)

list = [1, 2, 3, 4, 5]
list1 = [5,4,3,2,1]
for x in list:
    printleft(x)
print("    ")
for x in list1:
    printleft(x)
print("    ")
for x in list:
    printField(x)
print("    ")
for x in list:
    printField(-x)
print("    ")
