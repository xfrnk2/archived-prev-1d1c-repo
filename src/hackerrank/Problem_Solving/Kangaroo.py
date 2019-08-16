#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if v1 > v2 and (x1 - x2) % (v1 - v2) == 0:
        return "YES"
    else:
        return "NO"

