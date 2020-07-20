#!/bin/python3

import os
import sys


#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):

    for k, x in enumerate(grades):

        validSize = 1 <= k + 1 <= 60
        validScoreRange = 0 <= x <= 100
        if not (validSize and validScoreRange):
            print("Wrong Input")
            exit()

        if 38 <= x:
            value = 5 * (x // 5 + 1)
            if value - x < 3:
                grades[k] = value

    return grades
