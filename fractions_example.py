from math import gcd
import fractions
"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. 
Для проверки своего кода используйте модуль fractions.
"""


class MyFractions:
    def reduce_fraction(self):
        k = gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // k
        self.denominator = self.denominator // k

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.reduce_fraction()

    def __add__(self, other):
        res_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        res_denominator = self.denominator * other.denominator
        return MyFractions(res_numerator, res_denominator)

    def __mul__(self, other):
        return MyFractions(self.numerator * other.numerator, self.denominator * other.denominator)

    def __str__(self):
        if self.numerator == self.denominator:
            return "1"
        return f"{self.numerator}/{self.denominator}"


if __name__ == "__main__":
    str1 = input("Первая дробь a/b ")
    str2 = input("Вторая дробь a/b ")
    first_fraction = MyFractions(* map(int, str1.split(sep='/')))
    second_fraction = MyFractions(* map(int, str2.split(sep='/')))
    print(f"Сложение MyFractions {first_fraction + second_fraction}")
    print(f"Сложение fratcions {fractions.Fraction(str1) + fractions.Fraction(str2)}")
    print(f"Умножение MyFractions {first_fraction * second_fraction}")
    print(f"Умножение fractions {fractions.Fraction(str1) * fractions.Fraction(str2)}")
