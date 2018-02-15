# TODO - pip install raven

from raven import Client

# TODO - sentry 오류 보고 시스템에 대해서 학습합니다.
client = Client(
    'https://65d575d59e1748299f322af362a6b529:c4ba94596b824466a1a11631ec50623c@sentry.team504.co.kr//2')

try:
    # 1 / 0
    # 0으로 나누는 것 때문에 ZeroDivisionError가 발생하므로 해당 코드를 주석처리,
    # pass를 넣어서 대체.
    pass
except ZeroDivisionError:
    client.captureException()
