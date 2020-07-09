n = int(input())
answers = [0]*(n+1)
answers[1] = 0

for i in range(2, n + 1):
    answers[i] = answers[i - 1] + 1
    if i % 2 == 0 and answers[i] > answers[i // 2] + 1:
        answers[i] = answers[i // 2] + 1
    if i % 3 == 0 and answers[i] > answers[i // 3] + 1:
        answers[i] = answers[i // 3] + 1

print(answers[n])