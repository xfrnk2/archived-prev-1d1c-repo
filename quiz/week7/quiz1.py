"""
조금 쉬운 레스토랑 시뮬레이션 하기 길라잡이.


매 분 마다 레스토랑은 틱을 발생시킵니다.
매 틱 마다 레스토랑은 아래와 같이 출력합니다.
# TODO - 레스토랑 오픈 후 n분이 지났습니다.

"""

from raven import Client


class Restaurant:
    # TODO - 적절히 채워주세요.

    def __init__(self):
        self.__continue = True

    def run(self):
        turn = 0

        while self.__continue:
            # TODO - 적절히 채워주세요.

            turn += 1

            print(f"레스토랑 오픈 후 {turn}분이 지났습니다.")
            if turn == 720:
                self.__continue = False
                print("레스토랑을 종료합니다")

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
