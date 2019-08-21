import os
import sys

from src.hackerrank.Problem_Solving.CutTheSticks import cutTheSticks


class TestClass(object):
    def test_func(self):
        assert cutTheSticks([5, 4, 4, 2, 2, 8]) == [6, 4, 2, 1], "연산을 잘 수행한다"
        assert cutTheSticks([1, 2, 3, 4, 3, 3, 2, 1]) == [8, 6, 4,
                                                          1], "연산을 잘 수행한다"
