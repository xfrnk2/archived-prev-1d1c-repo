#https://www.acmicpc.net/problem/8958
number = int(input())
quizs = [input() for _ in range(number)]

for quiz in quizs:
    score = 0
    o_count = 1
    flag: bool = False
    for v in quiz:
        if v == "O":
            if flag:
                o_count += 1
            score += o_count
            flag = True
        else:
            o_count = 0
    print(score)


