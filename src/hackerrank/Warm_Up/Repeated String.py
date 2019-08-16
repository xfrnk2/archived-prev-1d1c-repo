#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

    l = len(s)
    findTarget = 'a'
    return s.count(findTarget) * (n // l) + s[:n % l].count(findTarget)
