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

손님은 도착 후 1~3분 뒤 1~5 사이의 무작위의 수를 이야기합니다.
아래와 같이 출력합니다.

# TODO - n번째 손님이 x분 고민을 하고, y라는 수를 말했습니다.

해당 손님은 해당 수를 이야기 한 뒤 1~10분 후 무작위로 돌아갑니다.

# TODO - n번째 손님이 도착한지 z분 만에 돌아갑니다.


"""

from raven import Client


class Restaurant:
    # TODO - 적절히 채워주세요.
    pass

    def run(self):
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
