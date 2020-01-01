#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    if x == y:
        return ("Mouse C")

    c1 = abs(y - z)
    c2 = abs(x - z)

    if c1 == c2:
        return ("Mouse C")
    if c1 > c2:
        return ("Cat A")
    return ("Cat B")

