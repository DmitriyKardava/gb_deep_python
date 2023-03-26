"""
Три друга взяли вещи в поход. Сформируйте словарь, где
ключ - имя друга, а значение - кортеж вещей. Ответьте на
вопросы:
📌 какие вещи взяли все три друга
📌 какие вещи уникальны, есть только у одного друга
📌 какие вещи есть у всех друзей кроме одного и имя того, у
кого данная вещь отсутствует
📌 Для решения используйте операции с множествами. Код
должен расширяться на любое большее количество друзей.
"""

hike = {"Петр": ("рюкзак", "топор", "спички", "сапоги", ),
        "Дмитрий": ("рюкзак", "спички", "сапоги", ),
        "Иван": ("палатка", "рюкзак", "спички", ),
        "Федор": ("рюкзак", "спички", "сапоги", ),
        "Марк": ("спички", "рюкзак", "топор", "сапоги", ),
        }
hike = {k: set(v) for k, v in hike.items()}

print(f"Взяли все: {set.intersection(*hike.values())}")
union = set.union(*hike.values())

hike_count = {}
for items in hike.values():
    for item in items:
        hike_count[item] = hike_count.get(item, 0) + 1

print("Есть только у одного человека:")
for key, val in hike_count.items():
    if val == 1:
        print(key)

print("Взяли все, кроме:")
for key, val in hike_count.items():
    if val == len(hike) - 1:
        for name, things in hike.items():
            if key not in things:
                print(key, name)