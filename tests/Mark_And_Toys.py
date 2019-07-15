import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from hackerrank.Interview_Preparation_Kit.Sorting.Mark_And_Toys import maximumToys


class TestClass(object):
    def test_func(self):
        assert maximumToys([], 0) == 0, "아무값도 안들어와도 잘 동작한다"
        assert maximumToys([1, 12, 5, 111, 200, 1000, 10], 50) == 4, "연산을 잘 처리한다"
        assert maximumToys([1, 2, 3, 4],
                           7) == 3, "연산을 잘 처리한다"
        assert maximumToys([3, 7, 2, 9, 4], 15) == 3, "연산을 잘 처리한다"
