"""
Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ - значение переданного аргумента, а значение - имя аргумента.
Если ключ не хэшируем, используйте его строковое представление.
"""


def my_func(**kwargs):
    result = {}
    for k, v in kwargs.items():
        if not v.__hash__:
            v = str(v)
        result[v] = k
    return result


print(my_func(a=[10], b=123, c="string", d=3.14))
