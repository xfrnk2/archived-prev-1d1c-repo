import random


# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3


def all_group():
    characters = "abcdefghijklmnopopqrwtuvwxyz"
    length = random.randrange(1, 21)
    names = []

    for x in range(1, 10001):
        name = "".join([random.choice(characters) for _ in range(length)])
        names.append(name)

    return names



def main():
    names = all_group()
    print(names[-1])


main()
