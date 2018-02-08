# coding=utf-8

"""
레스토랑을 시뮬레이션 해주세요.

손님은 3가지 조건이 있습니다.
도착 시간, 요리 주문 타입, 최대 대기 시간

일정 시간마다 무작위로 손님이 1명씩 도착합니다.
# TODO - 손님이 도착하면 화면에 손님이 도착했다는 문구를 출력해야 합니다.
# TODO - n번째 손님이 시각 xx 분에 레스토랑에 도착했습니다.

이 손님의 최대 대기 시간을 15분~40분까지 무작위로 설정합니다.
레스토랑의 현재 운영 상태로부터 대기 시간을 계산해서,
이 손님의 최대 대기 시간을 초과할 경우 손님은 기다리지 않고 그대로 돌아갑니다.
# TODO - 돌아갈 경우 화면에 이 손님이 돌아간다는 문구를 출력해야 합니다.
# TODO - 손님이 기다릴 수 없어 돌아갑니다.
# TODO - 현재 대기 시간 xx분 / 대기 가능 시간 xx분

손님이 최대 대기 시간 미만을 기다릴 경우, 대기 시간이 끝나면 손님은 자리에 착석을 하고
무작위로 요리를 1가지 주문합니다.
# TODO - 손님이 요리를 주문하면, 요리를 주문했다는 문구를 출력해야 합니다.
# TODO - n번 손님이 x번 테이블에 앉습니다.
# TODO - n번 손님이 i번 요리(oooo)를 주문합니다.

조리가 완료 되면 요리가 손님의 테이블에 도착하고, 손님은 식사를 시작합니다.
# TODO - 손님이 식사를 시작하면, 해당 문구를 출력해야 합니다.
# TODO - n번 손님의 i번 요리(oooo) 조리가 끝났습니다.
# TODO - n번 손님이 식사를 시작합니다.

식사가 완료 되면 손님은 계산대 앞에 가서 대기합니다.
# TODO - n번 손님이 식사를 마쳤습니다.
# TODO - n번 손님이 계산대 앞에 줄을 섭니다.

계산이 완료 되면 손님은 떠납니다.
# TODO - n번 손님이 계산을 마치고 레스토랑을 떠났습니다.


요리는 4가지 종류가 있습니다.

1. 스테이크 - 조리 시간 30분, 먹는 시간 30분
2. 스파게티 - 조리 시간 20분, 먹는 시간 20분
3. 마카로니 - 조리 시간 10분, 먹는 시간 15분
4. 그라탱   - 조리 시간 15분, 먹는 시간 10분

레스토랑에는 요리사가 3명이 있습니다.
한 요리사는 한 번에 1가지 요리를 할 수 있습니다.

레스토랑에는 테이블이 20개 있습니다.
모든 손님은 각각 한 테이블에 한 명씩 앉습니다.

계산대는 1개가 있습니다.
계산대에서는 홀 매니저가 계산을 하며 계산을 하는데는 5분이 소요 됩니다.

테이블이 비어있지 않으면 손님을 더 받을 수 없습니다.

하루 일과 시간 (720분) 동안 레스토랑의 장사를 시뮬레이션 해주세요.

모든 시간은 분 단위로 계산합니다.

이 과제는 그대로 심화 되어 다음 주로 계속 이어집니다.
언제나 코드를 작성할 때는 새로운 요구사항에 유연하게 대처 가능하도록
확장 가능하고 수정 및 유지보수가 편리하도록 고민해주세요.

"""
import random
from raven import Client


class Guest:
    def __init__(self):
        self.__arrival_time: int = None
        self.menu_type: int = None
        self.max_waiting_time: int = None

        self.__eating_time = 0

        self.guest_number = 0

        self.__menu = Menu()
        self.__chef = Chef()

    def set_max_waiting_time(self):
        time = random.randrange(15, 41)
        self.max_waiting_time = time()

    @property
    def set_menu_type(self):
        problem = random.randrange(0, 3)
        return problem

    def guest_simulate(self):
        guest = Guest()
        guest.set_menu_type()
        value = guest.set_menu_type
        self.menu_type = value

        guest.set_max_waiting_time()

        # 도착한 현재 시간도 얻어오자


class GuestVisit:
    def __init__(self):
        self.__GuestElapsedTime = 0
        self.__data = Guest()

    @staticmethod
    def checking_visited_guest() -> bool:

        machine = random.randrange(5)
        if machine == 2 or 3:
            return True

        else:
            return False

    def add_new_guest(self):

        self.checking_visited_guest()
        value = self.checking_visited_guest()
        if value is True:

            self.__data.guest_number += 1

            self.when_guest_visited()

            table = TableManager()
            table.simulate()

        else:
            pass

    def when_guest_visited(self):

        number = self.__data.guest_number
        time = Time.elapsed_time
        print(f"{number}번째 손님이 시각 '{time}' 분에 레스토랑에 도착했습니다.")


class Table:
    table = 20


class TableManager:

    def __init__(self):

        self.__tables = [0 for _ in range(Table.table)]
        self.__menu = Menu()
        self.__data = Guest()

    def simulate(self):
        number = self.__data.guest_number
        menu = self.__menu.set_menu
        order_number = self.__menu.get_order_number

        tables = self.__tables

        for y in range(Table.table):
            if tables[y] == 1:
                continue
            if y == Table.table - 1:
                if tables[y] == 1:
                    pass
                # TODO - 더이상 손님을 받을 수 없는 상황이 발생.
                # TODO - 요리사와 계산대의 소요 시간을 합산하여 총 대기시간을 계산한다.
                else:
                    tables[y] = 1
                    self.__menu.place_order()
                    print(f"{number}번 손님이 f{y}번 테이블에 앉습니다.")

                    print(f"{y}번 손님이 {order_number}번 요리{menu})를 주문합니다.")


            else:

                tables[y] = 1
                self.__menu.place_order()

                print(f"{number}번 손님이 {y}번 테이블에 앉습니다.")

                print(f"{y}번 손님이 {order_number}번 요리{menu}를 주문합니다.")


class Counter:
    def __init__(self):
        self.__own_time = 0
        self.status_of_counter = None
        self.__chef = Chef()

    def simulate(self):
        if self.status_of_counter is True:

            self.__own_time += 5
        else:
            pass

    def minus_time(self):
        if self.__own_time > 0:

            self.__own_time -= 1

        else:
            print("n번 손님이 계산을 마치고 레스토랑을 떠났습니다.")
            self.status_of_counter = False


class Menu:
    def __init__(self):  # , '스파게티','마카로니','그라탱':'15'
        self.__CookingTime = {'스테이크': 30, '스파게티': 20, '마카로니': 10, '그라탱': 15}
        self.__EatingTime = {'스테이크': 30, '스파게티': 20, '마카로니': 15, '그라탱': 10}
        self.__menu = {0: "스테이크", 1: "스파게티", 2: "마카로니", 3: "그라탱"}
        self.__order = None
        self.__guest = Guest()

    def get_cooking_time(self):
        getvalue = self.__CookingTime
        if self.__order == 0:
            return getvalue.get('스테이크')
        if self.__order == 1:
            return getvalue.get('스파게티')
        if self.__order == 2:
            return getvalue.get('마카로니')
        if self.__order == 3:
            return getvalue.get('그라탱')
        else:
            pass

    def get_eating_time(self):
        getvalue = self.__EatingTime
        if self.__order == 0:
            return getvalue.get('스테이크')
        if self.__order == 1:
            return getvalue.get('스파게티')
        if self.__order == 2:
            return getvalue.get('마카로니')
        if self.__order == 3:
            return getvalue.get('그라탱')

        else:
            pass

    def set_menu(self):
        menu_number = self.__order
        return self.__menu.get(menu_number)
        # 메뉴의 이름을 반환

    def get_order_number(self):
        return self.__order

    def place_order(self):

        menu = self.__guest.menu_type

        self.__order = menu


class Chefs:
    chefs = 3


class Chef:
    def __init__(self: int):
        self.__chef_first = None
        self.__chef_second = None
        self.__chef_third = None
        self.__works = [0 for _ in range(Chefs.chefs)]
        self.__menu = Menu()
        self.__counter = Counter()

    @staticmethod
    def print_finished_cooking():
        print("n번 손님의 i번 요리(oooo) 조리가 끝났습니다")
        print("n번 손님이 식사를 시작합니다")

    @staticmethod
    def print_finished_eating():
        print(" n번 손님이 식사를 마쳤습니다.")
        print(" n번 손님이 계산대 앞에 줄을 섭니다.")

    def reset_chef_time(self):
        if self.__chef_first == 0:
            self.__chef_first = None
            __class__.print_finished_eating()
            self.__counter.status_of_counter = True
        if self.__chef_second == 0:
            self.__chef_second = None
            __class__.print_finished_eating()
            self.__counter.status_of_counter = True
        if self.__chef_third == 0:
            self.__chef_third = None
            __class__.print_finished_eating()
            self.__counter.status_of_counter = True

        else:
            pass

    def minus_time(self):
        if self.__chef_first > 0:
            self.__chef_first -= 1
        if self.__chef_second > 0:
            self.__chef_second -= 1
        if self.__chef_third > 0:
            self.__chef_third -= 1
        else:
            __class__.reset_chef_time(self)

    def chef_simulate(self):

        chef = Chefs.chefs

        works = self.__works

        group = [self.__chef_first, self.__chef_second,
                 self.__chef_third]

        value = self.__menu.get_cooking_time()

        for x in range(chef):
            if works[x] == 1:
                continue
            if x == chef - 1:
                if works[x] == 1:
                    # 꽉 찼다
                    pass
                else:
                    works[x] = 1

                    group[x] = value

            else:
                works[x] = 1

                group[x] = value


class Time:
    elapsed_time = 0

    def __init__(self):
        self.__chef = Chef()
        self.__counter = Counter()
        self.__guest = Guest()
        self.__guest_visit = GuestVisit

    def tick(self):
        for x in range(720):
            Time.elapsed_time += 1
            print(f"현재시간 {Time.elapsed_time}/720분)")

            self.__guest.guest_simulate()
            self.__guest_visit.add_new_guest()

            self.__chef.minus_time()
            self.__counter.minus_time()

            self.__chef.chef_simulate()
            self.__chef.reset_chef_time()
            self.__counter.simulate()

            # get 걸리는 시간을 얻어온다. 매 틱 마다 한번씩 모든 장소를 반복 실행함.


client = Client(
    'https://65d575d59e1748299f322af362a6b529'
    ':c4ba94596b824466a1a11631ec50623c@sentry.team504.co.kr//2')

if __name__ == '__main__':
    # noinspection PyBroadException
    try:
        pass
    except Exception:
        client.captureException()
