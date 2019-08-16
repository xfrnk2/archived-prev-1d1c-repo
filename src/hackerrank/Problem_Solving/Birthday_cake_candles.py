#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    mx = ar[0]
    candle = 0
    for x in ar:

        if mx < x:
            mx = x
            candle = 0
        if mx == x:
            candle += 1

    return candle
