import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from hackerrank.Problem_Solving.Equalize_The_Array import equalizeArray


class TestClass(object):
    def test_func(self):
        assert equalizeArray([3, 3, 2, 1, 3]) == 2, "연산을 잘 수행한다"
        assert equalizeArray([1, 2, 3, 1, 2, 3, 3, 3]) == 4, "연산을 잘 수행한다"