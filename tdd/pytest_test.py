# 링크 : https://docs.pytest.org/en/latest/getting-started.html
import pytest


def func_test(x):
    return x + 1

# def test_answer():
#     assert func_test(3) == 5
#


def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()


class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    # def test_two(self):
    #     x = "hello"
    #     assert hasattr(x, 'check')

#
# def test_needsfiles(tmpdir):
#     print(tmpdir)
#     assert 0

# 테스트가 예외처리를 잘 하므로 travis ci에 검출되지 않도록 주석 처리
# if __name__ == 'main__':
#     test_answer()
