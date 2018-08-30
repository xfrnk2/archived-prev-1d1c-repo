from raven import Client


def calandar():
    for x in range(1, 13):
        print("\n")
        for y in range(1, 32):
            value = x % 2
            if x <= 7:
                if value == 0:
                    if y == 31:
                        break

            elif 8 <= x:
                if value == 1:
                    if y == 31:
                        break
            print(f"{x}월 , {y}일")


client = Client(
    'https://65d575d59e1748299f322af362a6b529'
    ':c4ba94596b824466a1a11631ec50623c@sentry.team504.co.kr//2')

if __name__ == '__main__':
    # noinspection PyBroadException

    try:
        calandar()
    except Exception:
        client.captureException()
