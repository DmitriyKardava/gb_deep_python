import unittest


class TestFibonacci(unittest.TestCase):

    def setUp(self) -> None:
        self.f = Fibonacci()

    def test0(self):
        self.assertEqual(self.f(0), 0)

    def test1(self):
        self.assertEqual(self.f(1), 1)

    def test3(self):
        self.assertEqual(self.f(3), 2)


class Fibonacci:
    def __call__(self, n: int):
        fib1, fib2 = 0, 1
        for i in range(n):
            fib1, fib2 = fib2, fib1 + fib2
        return fib1


if __name__ == '__main__':
    unittest.main(verbosity=2)
