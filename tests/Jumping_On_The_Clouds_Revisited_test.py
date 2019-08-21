import sys
import os

from src.hackerrank.Problem_Solving.Jumping_On_The_Clouds_Revisited import jumping_on_clouds


class TestClass(object):
    def test_func(self):

        assert jumping_on_clouds([1, 1, 1, 0, 1, 1, 0, 0, 0, 0], 3) == 94, "연산을 잘 수행한다"
        assert jumping_on_clouds([0, 0, 1, 0, 0, 1, 1, 0], 2) == 92, "연산을 잘 수행한다"
