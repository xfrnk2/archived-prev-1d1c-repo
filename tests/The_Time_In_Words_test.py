import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from hackerrank.Problem_Solving.The_Time_In_Words import timeInWords


class TestClass(object):
    def test_func(self):
        assert timeInWords(5, 47) == "thirteen minutes to six", "연산을 잘 수행한다"
        assert timeInWords(10, 57) == "three minutes to eleven", "to 사용이 올바르다"
        assert timeInWords(10, 6) == "six minutes past ten", "past 사용이 올바르다"
        assert timeInWords(3, 00) == "three o' clock", "정각에 맞는 시간을 리턴한다"
        assert timeInWords(1, 1) == "one minute past one", "minute를 복수형이 아닌 단수형으로  잘 처리한다"