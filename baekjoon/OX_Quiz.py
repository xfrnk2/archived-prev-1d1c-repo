number = int(input())
quizs = [input() for _ in range(number)]

for quiz in quizs:
    score = o_count = 0
    temp = ""
    for v in quiz:
        if v == "O":
            score += (1 + o_count)
            if temp == "O":
                o_count += 1
            temp = "O"
        else:
            o_count = 0
    print(score)


