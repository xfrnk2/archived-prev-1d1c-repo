# coding=utf-8

from week6.chef import Chef
from week6.menu import Menu
import random


class Guest:
    def __init__(self):
        self.__arrival_time: int = None
        self.menu_type: int = None
        self.max_waiting_time: int = None

        self.__eating_time = 0

        self.guest_number = 0

        self.__menu = Menu()

        # FIXME - 손님이 요리사를 알아야 할 필요가 있을까요?
        self.__chef = Chef()

    def set_max_waiting_time(self):
        # FIXME - 이런 상수(변하지 않는) 숫자 값은 유의미한 변수명을 정의해서
        # 그 뜻을 명확히 하는 편이 좋습니다.

        min_duration = 15
        max_duration = 41

        cooking_duration = random.randrange(min_duration, max_duration)

        time = random.randrange(15, 41)
        self.max_waiting_time = time()

    @property
    def set_menu_type(self):
        # FIXME - 아래와 같이 한 줄로 반환 가능합니다.
        # return random.randrange(0, 3)

        # FIXME - 아래의 0~3 역시 위에서 언급한 것처럼 상수를 변수명을 붙여주세요.
        # 언제, 누가 보더라도 뜻을 명확하게 파악 할 수 있어야 합니다.

        return problem

    def guest_simulate(self):
        # FIXME - 자신의 내부에서 자신을 생성하는 것은 좋은 방식이 아닌 것 같습니다.
        guest = Guest()
        guest.set_menu_type()
        value = guest.set_menu_type
        self.menu_type = value

        guest.set_max_waiting_time()

        # 도착한 현재 시간도 얻어오자
