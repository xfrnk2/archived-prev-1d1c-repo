import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from src.hackerrank.Problem_Solving.Jumping_On_The_Clouds_Revisited import jumpingOnClouds


class TestClass(object):
    def test_func(self):
        assert jumpingOnClouds([1, 1, 1, 0, 1, 1, 0, 0, 0, 0], 3) == 94, "연산을 잘 수행한다"
        assert jumpingOnClouds([0, 0, 1, 0, 0, 1, 1, 0], 2) == 92, "연산을 잘 수행한다"
