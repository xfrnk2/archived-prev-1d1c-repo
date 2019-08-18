#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    v = 0
    for i, j in enumerate(bill):
        if i == k:
            continue
        else:
            v += j

    v = v // 2

    if b == v:
        print("Bon Appetit")
    else:
        print(b - v)

