from src.hackerrank.Interview_Preparation_Kit.Sorting.Bubble_Sort import countSwaps


class TestClass(object):
    def test_func(self):
        assert countSwaps([1, 2, 3]) == (0, 1, 3), "연산을 잘 수행한다"
        assert countSwaps([4, 2, 3, 1]) == (5, 1, 4), "연산을 잘 수행한다"
        assert countSwaps([1]) == (0, 0, 0), "인자로 받아온 배열의 길이가 1이면 0을 리턴한다"

