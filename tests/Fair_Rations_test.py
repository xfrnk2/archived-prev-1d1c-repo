from src.hackerrank.Problem_Solving.Fair_Rations import fairRations


class TestClass(object):
    def test_func(self):
        assert fairRations([1, 2]) == "NO", "리스트 길이가 2인 조건에서 연산을 잘 수행한다."
        assert fairRations([2, 2]) == 0, "리스트 길이가 2인 조건에서 연산을 잘 수행한다."
        assert fairRations([1, 1]) == 2, "리스트 길이가 2인 조건에서 연산을 잘 수행한다."
        assert fairRations([1, 2, 4]) == "NO", "연산을 잘 수행한다"
        assert fairRations([1, 3, 6]) == 2, "연산을 잘 수행한다"
