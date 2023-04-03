import pytest


def test_fib():
    f = Fibonacci()
    assert f(0) == 0
    assert f(1) == 1
    assert f(3) == 2


class Fibonacci:
    def __call__(self, n: int):
        fib1, fib2 = 0, 1
        for i in range(n):
            fib1, fib2 = fib2, fib1 + fib2
        return fib1


if __name__ == '__main__':
    pytest.main(['-vv'])
