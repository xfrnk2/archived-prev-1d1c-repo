# coding=utf-8

# TODO - pip install raven

from raven import Client

# TODO - sentry 오류 보고 시스템에 대해서 학습합니다.
client = Client('https://65d575d59e1748299f322af362a6b529:c4ba94596b824466a1a11631ec50623c@sentry.team504.co.kr//2')

try:
    # FIXME - 여전히 오류가 발생하고 있습니다.
    1 / 0
except ZeroDivisionError:
    client.captureException()