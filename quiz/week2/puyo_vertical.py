# 필드를 네모로 출력한다
# 출력한 네모를 까만 네모로 바꿔 끼운다

# 리스트를 만든다. 5x5의 리스트. 다음은 위치를 지정한다. 배열 만들기 -> 배열 순서 -> 클리어

import time
import os

"""
def clear():
    os.system('cls')
"""

# 0, 2
# 1, 2
#  2, 2
#   3, 2
#    4, 2

class Simulate():
    def __init__(self):
        self.__continue = True
        self.__list = {}

    def __str__(self):
        return '{}'.format(self.__list)

    def run(self):
        turn = 0
        while self.__continue:

            if turn == 6:
                print("종료합니다")
                self.__continue = False

            self.__list.update({0: Field()})
            print(self.__list.values)

            for key, value in self.__list.items():

                value.tick()
                value.set_field()
                value.change_area()
                value.print_field()
                time.sleep(1)
                turn += 1


class Field():

    def __init__(self):
        self.__value = ['□' for _ in range(5)]
        self.__array1 = []
        self.__array2 = []

        self.__block_area = 0
        self.__block = "■"

    def __str__(self):
        return "{}".format(self.__block)

    def tick(self):
        self.__block_area += 1

    def change_area(self):
        #TODO -  스킬이 필요하다. 배열에 문자열을 직접 삽입은 못하지만 기술적인 방법으로 할 수 있을 것 같다. 우선 시간이 오래 걸릴것 같은이 보류.

        self.__array2[self.__block_area][2] = self.__block

    def set_field(self):
        value = ' '.join(self.__value) + "\n"

        self.__array1 = [value for _ in range(5)]

        self.__array2 = ' '.join(self.__array1) + "\n"

    def print_field(self):
        print(self.__array2, end=" ")







if __name__ == '__main__':
    """
      # join의 사용법
  
      l = [ 'hello', 'world', '1234']
  
      result1 = ' '.join(l)
      result2 = ','.join(['a', 'b', 'c'])
  
      print(result1)
      print(result2)
      
      
  """
    aaa = Simulate()
    aaa.run()
