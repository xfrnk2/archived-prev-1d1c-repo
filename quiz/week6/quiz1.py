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
        self.__ArrivalTime: int = None
        self.__MenuType: int = None
        self.MaximumWatingTime: int = None

    def SetMaximumWatingTime(self):
        time = random.randrange(15, 41)
        self.MaximumWatingTime = time()

    def SetMenuType(self):
        setmenu = random.randrange(0, 3)
        return setmenu


class GuestVisit:
    def __init__(self):
        self.__GuestElapsedTime = 0
        self.__data = Guest()

    def GuestVisitTimer(self) -> bool:

        machine = random.randrange(5)
        if machine == 2 or 3:
            return True

        else:
            return False

    def AddNewGuest(self):
        if self.GuestVisitTimer() is True:
            Time.elapsed_time += 1
            self.__GuestElapsedTime += 1
            GuestNumber.people += 1

            self.WhenGuestVisited()
        if self.GuestVisitTimer() is False:
            Time.elapsed_time += 1
            self.__GuestElapsedTime += 1

    def WhenGuestVisited(self):
        number = GuestNumber.people
        time = Time.elapsed_time
        print("f'{number}'번째 손님이 시각 f'{time}' 분에 레스토랑에 도착했습니다.")

    def GuestGoHome(self):
        maximum = self.__data.MaximumWatingTime
        guestelapsedtime = self.__GuestElapsedTime
        if maximum < guestelapsedtime:
            print("손님이 기다릴 수 없어 돌아갑니다.")
            print("현재 대기시간 f'{guestelapsedtime}'분, 대기 가능시간 f'{maximum}'분 ")
        # 손님이 꽉 찼을때의 조건을 추가해야 한다.


class TableManager:
    def __init__(self):
        self.__tables = None

    def simulate(self):

        max_table_quantity = 20
        self.__tables = tables = [0 for _ in range(max_table_quantity)]
        if GuestVisit.GuestVisitTimer is True:
            for y in range(max_table_quantity):
                if tables[y] == 1:
                    continue
                if y == max_table_quantity - 1:
                    # TODO - 아직 어떻게 해야 할지 몰라 미구현. 일단 나중에 구현하자
                    pass

                # 더이상 손님을 받을 수 없는 상황이 발생한다.
                else:
                    tables[y] = 1


class Counter:
    pass


class Menu:
    def __init__(self):  # , '스파게티','마카로니','그라탱':'15'
        self.__CookingTime = {'스테이크': 30, '스파게티': 20, '마카로니': 10, '그라탱': 15}
        self.__EatingTime = {'스테이크': 30, '스파게티': 20, '마카로니': 15, '그라탱': 10}
        self.__order = None

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


class Chef:
    pass


class Time:
    elapsed_time = 0.0
    current_time = 0.0


class GuestNumber:
    people = 0


client = Client(
    'https://65d575d59e1748299f322af362a6b529'
    ':c4ba94596b824466a1a11631ec50623c@sentry.team504.co.kr//2')

if __name__ == '__main__':
    # noinspection PyBroadException
    try:
        pass
    except Exception:
        client.captureException()
