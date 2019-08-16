#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    if s1.intersection(s2):
        return("YES")
    return("NO")
