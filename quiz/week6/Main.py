# coding=utf-8

from raven import Client

client = Client(
    'https://65d575d59e1748299f322af362a6b529'
    ':c4ba94596b824466a1a11631ec50623c@sentry.team504.co.kr//2')

if __name__ == '__main__':
    # noinspection PyBroadException
    try:
        print("레스토랑을 시작합니다.")

        print("레스토랑을 종료합니다.")
    except Exception:
        client.captureException()
