"""
Функция получает на вход словарь с названием компании в
качестве ключа и списком с доходами и расходами (3-10
чисел) в качестве значения.
Вычислите итоговую прибыль или убыток каждой компании.
Если все компании прибыльные, верните истину, а если хотя
бы одна убыточная - ложь.
"""


def profit(companies: []):
    total_profit = {}
    result = True
    for company in companies:
        for k, v in company.items():
            s = sum(v)
            if s < 0:
                result = False
            total_profit[k] = s
    print(total_profit)
    return result


my_companies = [
    {'company1': [1, 2, 3, 4]},
    {'company2': [1, 2, 3, 5]},
    {'company3': [10, 20, -50]},
]
profit(my_companies)
