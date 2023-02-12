"""
Напишите однострочный генератор словаря, который принимает на вход три
списка одинаковой длины: имена str, ставка int, премия str с указанием
процентов вида “10.25%”. В результате получаем словарь с именем в качестве
ключа и суммой премии в качестве значения. Сумма рассчитывается как
ставка умноженная на процент премии
"""
from decimal import Decimal


def bonus_calc(names, salaries, bonuses):
    return {name: salary * (Decimal(bonus.strip("%")) / 100)
            for name, salary, bonus in zip(names, salaries, bonuses)}


print(bonus_calc(['Иван'], [500], ["10%"]))
