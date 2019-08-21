from src.hackerrank.Problem_Solving.Equalize_The_Array import equalizeArray


class TestClass(object):
    def test_func(self):
        assert equalizeArray([3, 3, 2, 1, 3]) == 2, "연산을 잘 수행한다"
        assert equalizeArray([1, 2, 3, 1, 2, 3, 3, 3]) == 4, "연산을 잘 수행한다"
        assert equalizeArray([]) == 0, "인자로 빈 배열을 받으면 0을 리턴한다"
        assert equalizeArray(None) == 0, "아무 값도 안 들어올 경우에도 잘 동작한다"