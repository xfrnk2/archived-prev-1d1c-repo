#!/bin/python3

import os
import sys


#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):

    for k, x in enumerate(grades):

        if not 1 <= k + 1 <= 60 or not 0 <= x <= 100:
            print("Wrong Input")
            exit()

        if 38 <= x:
            value = 5 * (x // 5 + 1)
            if value - x < 3:
                grades[k] = value

    return grades


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for x in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
