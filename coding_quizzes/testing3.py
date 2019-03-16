from string import ascii_lowercase


def solution(word):
    if not isinstance(word, str) or not 1 <= len(word) <= 1000:
        print("잘못된 입력입니다")
        exit()

    answer = ''
    alphabet_low = list(ascii_lowercase)
    alphabet_low = ''.join(alphabet_low)
    alphabet_big = alphabet_low.upper()

    for x in word:

        if x.isalpha():

            if x.isupper():
                index = alphabet_big.index(x) + 1
                index *= - 1
                value = alphabet_big[index]
            else:
                index = alphabet_low.index(x) + 1
                index *= -1
                value = alphabet_low[index]

        else:
            value = x
        answer += value

    return (answer)


word = "I love you"
solution(word)
