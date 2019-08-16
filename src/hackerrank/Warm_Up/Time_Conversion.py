#!/bin/python3

import os
import sys


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    str_s = ''.join(s)
    hour = str_s[:2]

    if str_s[8] == 'P':
        if hour == '12':
            pass
        else:
            hour = str(int(hour) + 12)
        return hour + str_s[2:8]

    elif str_s[8] == 'A':

        if hour == '12':
            hour = '00'
        return hour + str_s[2:8]

    #


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
