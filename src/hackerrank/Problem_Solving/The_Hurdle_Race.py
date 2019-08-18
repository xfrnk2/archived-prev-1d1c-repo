#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hurdleRace function below.
def hurdleRace(k, height):
    max_value = max(height)
    if k > max_value:
        return 0
    return max_value - k
