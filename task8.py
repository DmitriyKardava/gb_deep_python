"""Создайте несколько переменных заканчивающихся и не
оканчивающихся на “s”. Напишите функцию, которая при запуске заменяет
содержимое переменных оканчивающихся на s (кроме
переменной из одной буквы s) на None.
Значения не удаляются, а помещаются в одноимённые
переменные без s на конце.
"""


def change_vars():
    variables = dict(globals())
    for k, v in variables.items():
        if not (k.startswith('__') and k.endswith('__')):
            if len(k) != 1 and k.endswith('s') and not callable(v):
                globals()[k] = None
                globals()[k[:-1]] = v


a = 1
b = 4
s = 2
lists = [123, 456]
end_to_s = 'some text'
change_vars()
print(f"{lists=}")
print(f"{list=}")
print(f"{end_to_s=}")
print(f"{end_to_=}")
