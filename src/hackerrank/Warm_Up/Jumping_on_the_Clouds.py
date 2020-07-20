#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):


    steps = 0
    point = 0

    while  point < len(c) - 1:


        if c[point] == 0:
            if c[point + 1] == 0:

                if point == len(c) - 2:
                    if c[point + 1] == 0:
                        point += 1
                else:
                    if c[point + 2] == 0:
                        point += 2
                    else:
                        point += 1

            else:
                point += 2
            steps += 1

        return steps
