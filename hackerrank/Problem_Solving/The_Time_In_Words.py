def timeInWords(h, m):
    words = {"00": "o' clock", "01": "one", "02": "two", "03": "three",
             "04": "four", "05": "five", "06": "six", "07": "seven",
             "08": "eight",
             "09": "nine", "10": "ten", "11": "eleven", "12": "twelve",
             "13": "thirteen",
             "14": "fourteen", "15": "quarter", "16": "sixteen",
             "17": "seventeen", "18": "eighteen",
             "19": "nineteen", "20": "twelve", "21": "twenty one",
             "22": "twenty two", "23": "twenty three",
             "24": "twenty four", "25": "twenty five", "26": "twenty six",
             "27": "twenty seven",
             "28": "twenty eight", "29": "twenty nine", "30": "half"}
    h, m = str(h), str(m)

    if m == "0":
        return words["0" + h] + " " + words[m + m]

    flag = "past"
    if 30 < int(m):
        flag = "to"
        h = int(h) + 1
        m = 60 - int(m)
        h, m = str(h), str(m)

    if m == "30" or m == "15":

        if 10 <= int(h):
            return words[m] + " " + flag + " " + words[h]
        return words[m] + " " + flag + " " + words["0" + h]
    else:
        if 10 <= int(h):
            return words[m] + " " + "minutes" + " " + flag + " " + words[h]

        return words[m] + " " + "minutes" + " " + flag + " " + words["0" + h]


