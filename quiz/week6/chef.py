from week6.counter import Counter
from week6.menu import Menu


# FIXME - 쓸데 없이 분리 된 클래스. Chef 클래스 안에 선언 했어도 되었을텐데요...
class Chefs:
  value = 3


class Chef:
    def __init__(self: int):
        self.__chef_first = None
        self.__chef_second = None
        self.__chef_third = None
        self.__works = [0 for _ in range(Chefs.value)]
        self.__menu = Menu()

        # FIXME - Chefs 가 쉐프를 모아둔 일종의 매니저 클래스라면...
        # Chefs 클래스는 한 명의 요리사 역할만 수행해야 할 것이 아닐런지?
        self.__works = [0 for _ in range(Chefs.value)]

        # FIXME - 어째서 여기에 메뉴가 있는지?
        self.__menu = Menu()

        # FIXME - 어째서 여기에 카운터가 있는지?
        self.__counter = Counter()

    @staticmethod
    def print_finished_cooking():

        # FIXME - n을 어떻게 전달 받고 출력할지 고민해 주세요.
        print("n번 손님의 i번 요리(oooo) 조리가 끝났습니다")
        print("n번 손님이 식사를 시작합니다")

    @staticmethod
    def print_finished_eating():
        print(" n번 손님이 식사를 마쳤습니다.")
        print(" n번 손님이 계산대 앞에 줄을 섭니다.")

    def reset_chef_time(self):

        # FIXME - 이런 식의 하드 코딩은 좋지 않습니다.
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

    def minus_time(self):

        # FIXME - 여기도 마찬가지...
        if self.__chef_first > 0:
            self.__chef_first -= 1
        if self.__chef_second > 0:
            self.__chef_second -= 1
        if self.__chef_third > 0:
            self.__chef_third -= 1
        else:
            __class__.reset_chef_time(self)

    def chef_simulate(self):

        # FIXME - 클래스 간의 역할 고려 및 분할을 충분히 정립하지 않은 채로
        # 단순히 쪼개서 기능을 여기저기 우겨 넣은 흔적이 보입니다.
        # 그래서 코드가 전체적으로 분리 되지 않고 거미줄처럼 상호 복합적으로 얽혀서 복잡해졌어요.
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
