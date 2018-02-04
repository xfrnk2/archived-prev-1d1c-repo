# coding=utf-8


from game import Game
from raven import Client

Raven = Client('https://65d575d59e1748299f322af362a6b529:c4ba94596b824466'
               'a1a11631ec50623c@sentry.team504.co.kr//2')

if __name__ == '__main__':
    # noinspection PyBroadException
    try:
        game = Game()
        game.run()
    except Exception:
        Raven.captureException()
