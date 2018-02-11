# coding=utf-8

from week6.guest import Guest


# FIXME - 왜 이런 복잡한 형태를 만들었나...
# 예를 들면 최상위 클래스 하나를 만들어 놓고,
# 그 클래스를 상속 받는 구체적인 요리별 클래스를 정의하는 방향으로 가야 합니다.

# 그리고 최상위 공통 클래스가 요리 시간이나, 먹는데 걸리는 시간 등을 처리하는 로직을 담당하고,
# 개발 메뉴 클래스들이 고유 식별자 등을 처리하면 됩니다.

# 이런 충분한 클래스에 대한 고려가 없다보니 아래처럼 하드 코딩에
# 복사 후 붙여넣기 형태로 계속 반복 되는 중복 코드가 자꾸 보이게 됩니다.

class Menu:
    def __init__(self):  # , '스파게티','마카로니','그라탱':'15'
        self.__CookingTime = {'스테이크': 30, '스파게티': 20, '마카로니': 10, '그라탱': 15}
        self.__EatingTime = {'스테이크': 30, '스파게티': 20, '마카로니': 15, '그라탱': 10}
        self.__menu = {0: "스테이크", 1: "스파게티", 2: "마카로니", 3: "그라탱"}
        self.__order = None
        self.__guest = Guest()

    def get_cooking_time(self):

        # FIXME - 딕셔너리는 이런 형태로 사용하는 것이 아닙니다.
        # 딕셔너리의 사용 방식을 기초부터 다시 연습해 주세요.
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

        # FIXME - 주석은 아래와 같이 해당 라인의 밑에 적는게 아닙니다.
        # 관행적으로 보통 자신이 부연 설명할 코드의 위, 또는 우측 라인 끝에 적습니다.
        # 메뉴의 이름을 반환

    # FIXME - 아래와 같은 간단한 get 함수는 @property 를 활용하면 좋습니다.
    # 다른 사람의 코드를 자주 보고 분석, 공부, 따라하기 해보는 습관을 들여주세요.
    # 남의 코드를 계속 보면서 배워나가고, 자신의 것으로 만들어야 합니다.
    def get_order_number(self):
        return self.__order

    def place_order(self):

        menu = self.__guest.menu_type

        self.__order = menu
