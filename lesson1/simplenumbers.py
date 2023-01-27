MIN_NUM = 0
MAX_NUM = 100_000
while True:
    num = int(input(f"Введите число от {MIN_NUM} до {MAX_NUM}: "))
    if MIN_NUM <= num <= MAX_NUM:
        break
i = 3
while num % i != 0:
    if num % 2 == 0 or num <= 2:
        break
    i += 2
if num == i or num == 2:
    print(f"Число {num} простое")
else:
    print(f"Число {num} составное")
