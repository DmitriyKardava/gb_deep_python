"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
строковое представление. Функцию hex используйте для проверки своего результата.
"""


HEX_DICT = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
num = int(input("Введите число: "))
print(hex(num))
result = []
while num > 0:
    result.append(HEX_DICT[num % 16])
    num = num // 16
result.reverse()
print(f"0x{''.join(result)}")
