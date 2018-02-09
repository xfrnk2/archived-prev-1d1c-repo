# coding=utf-8


from raven import Client

client = Client(
    'https://65d575d59e1748299f322af362a6b529'
    ':c4ba94596b824466a1a11631ec50623c@sentry.team504.co.kr//2')

if __name__ == '__main__':
    # noinspection PyBroadException
    try:
        # FIXME - 일단 어떻게든 돌아가는 형태로 만들어주세요.
        # 윤곽만이라도 돌아가는 척 하는 형태만이라도 좋습니다.
        # 그렇게 작은 규모로 간단, 단순하게 만들어 놓고 조금씩 살을 붙이는 연습을 해야 합니다.

        # 처음부터 너무 많은 것을 하려고 잘게 쪼개고,
        # 제대로 충분한 고민과 정리 없이 클래스를 너무 찍어내기만 하는 기교를 부린 듯한 느낌을 줍니다.

        # 클래스는 무조건 만드는 것이 아니라
        # 필요한 역할 단위로 쪼개서 해야 할 일을 분담해야 하는 것입니다.

        # 클래스부터 정의하고 역할을 부여하지 마시고,
        # 역할 명세를 먼저 정한 후에, 해당 역할을 수행해야 할 주체를 나눠주세요.

        pass
    except Exception:
        client.captureException()
