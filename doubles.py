"""
Дан список повторяющихся элементов. Вернуть список с дублирующимися
элементами. В результирующем списке не должно быть дубликатов.
"""

test_data = [456, 10, 10, 23, 11, 123, 66, 78, 123, 456, 12]
counter = {}

for elem in test_data:
    counter[elem] = counter.get(elem, 0) + 1

doubles = [element for element, count in counter.items() if count > 1]

print(doubles)
