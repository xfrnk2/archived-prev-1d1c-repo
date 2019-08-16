import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from src.hackerrank.Problem_Solving.Beautiful_Triplets import beautifulTriplets


class TestClass(object):
    def test_func(self):
        assert beautifulTriplets(0, [1, 2, 4, 5, 7, 8, 10]) == 0, "d값에 0이면 0을 리턴한다"
        assert beautifulTriplets(1, []) == 0, "arr가 빈 리스트이면 0을 리턴한다"
        assert beautifulTriplets(3,
                                 [1, 2, 4, 5, 7, 8, 10]) == 3, "연산을 잘 처리한다"
        assert beautifulTriplets(3,
                                 [1, 6, 7, 7, 8, 10, 12, 13, 14, 19]) == 2, "연산을 잘 처리한다"
        assert beautifulTriplets(10,
                                 [1, 6, 7, 7, 8, 10, 12, 13, 14,
                                  19]) == 0, "연산을 잘 처리한다"

