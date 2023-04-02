class Fibonacci:
    """
    >>> f = Fibonacci()
    >>> print(f(0))
    0
    >>> print(f(1))
    1
    >>> print(f(3))
    2
    """
    def __call__(self, n: int):
        fib1, fib2 = 0, 1
        for i in range(n):
            fib1, fib2 = fib2, fib1 + fib2
        return fib1


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
