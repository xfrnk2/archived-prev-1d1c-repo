def timeInWords(h, m):
    words = {00: "o' clock", 1: "one", 2: "two", 3: "three",
             4: "four", 5: "five", 6: "six", 7: "seven",
             8: "eight",
             9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
             13: "thirteen",
             14: "fourteen", 15: "quarter", 16: "sixteen",
             17: "seventeen", 18: "eighteen",
             19: "nineteen", 20: "twelve", 21: "twenty one",
             22: "twenty two", 23: "twenty three",
             24: "twenty four", 25: "twenty five", 26: "twenty six",
             27: "twenty seven",
             28: "twenty eight", 29: "twenty nine", 30: "half"}

    minutes, flag, hours = "", " past ", " "

    if m == 0:
        return words[h] + " " + words[m]

    if 30 < m:
        flag = " to "
        m, h = 60 - m, h + 1

    minutes = words[m]
    hours = words[h]

    if m % 15 == 0:
        pass
    else:
        v = " minute"
        if 1 < m <= 60:
            v += "s"
        minutes += v

    return minutes + flag + hours