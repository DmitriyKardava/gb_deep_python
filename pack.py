pack = {"Палатка": 9,
        "Топор": 2,
        "Примус": 1,
        "Лопата": 4,
        "Фонарь": 3,
        }

a = tuple(pack.keys())
MAX_WEIGHT = 12
for i in range(len(a)):
    for j in range(i, len(a)):
        combo = (*a[:i], a[j])
        weight = 0
        for item in combo:
            weight += pack[item]
        if weight <= MAX_WEIGHT:
            print(combo, weight)
