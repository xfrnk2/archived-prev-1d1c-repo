# coding=utf-8

"""
조금 쉬운 레스토랑 시뮬레이션 하기 길라잡이.

quiz1.py 에서 작성한 레스토랑을 조금 더 세빌하게 수정합니다.

매 분 마다 레스토랑은 틱을 발생시킵니다.
매 틱 마다 레스토랑은 아래와 같이 출력합니다.
# TODO - 레스토랑 오픈 후 n분이 지났습니다.

3분마다 손님이 한 명씩 도착합니다.
아래와 같이 출력합니다.

# TODO - n번째 손님이 도착했습니다.

해당 손님은 1~10분 후 무작위로 돌아갑니다.

# TODO - n번째 손님이 도착한지 x분 만에 돌아갑니다.


"""

from raven import Client
import random


class Restaurant:

    def __init__(self):
        self.__continue = True
        self.__list = {}


    def run(self):
        turn = 0
        number = 1
        while self.__continue:
            # TODO - 적절히 채워주세요.

            turn += 1

            assert turn <= 720

            print(f"레스토랑 오픈 후 {turn}분이 지났습니다.")

            if self.__list:

                for key, value in self.__list.items():

                    if not value.tick():
                        self.__list.pop(key)

                        time = value.get_staying_time
                        print(f"{key}번째 손님이 도착한지"
                              f" {time}분 만에 돌아갑니다.")

            if turn % 3 == 0:
                self.__list.update({number: Guest()})
                number += 1
            else:
                pass

    def set_staying_time(self):
        return random.randrange(1, 11)


class Guest:
    def __init__(self):
        self.__number = 0
        self.__time = 0
        self.current_time = 0

    def information(self, number, time):
        self.__number = number
        self.__time = time

    def get_staying_time(self):
        return self.__time

    def tick(self):

        if self.current_time == self.__time:
            return False
        else:
            pass

client = Client(
    'https://65d575d59e1748299f322af362a6b529'
    ':c4ba94596b824466a1a11631ec50623c@sentry.team504.co.kr//2')

if __name__ == '__main__':
    # noinspection PyBroadException
    try:
        r = Restaurant()
        r.run()

    except Exception:
        client.captureException()
