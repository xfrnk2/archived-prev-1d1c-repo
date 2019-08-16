#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the rotLeft function below.
def rotLeft(a, d):
    size = len(a)

    if size <= 1:
        pass

    if size < d:
        print("Wrong Input")
        exit()

    else:
        temp = a[:d]
        a = a[d:]

        a.extend(temp)

    return a