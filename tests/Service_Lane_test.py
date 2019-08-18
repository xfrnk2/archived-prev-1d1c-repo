import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from src.hackerrank.Problem_Solving.Service_Lane import serviceLane


class TestClass(object):
    def test_func(self):
        assert serviceLane(8,[(0, 3), (4, 6), (6, 7), (3, 5), (0, 7)],[2, 3, 1, 2, 3, 2, 3,
                                                 3]) == [1, 2, 3, 2, 1], "코드가 잘 동작한다"