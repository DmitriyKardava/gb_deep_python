MIN_NUM = 0
MAX_NUM = 100_000
FIRST_SIMPLE_NUM = 2
while True:
    num = int(input(f"Введите число от {MIN_NUM} до {MAX_NUM}: "))
    if MIN_NUM <= num <= MAX_NUM:
        break
i = FIRST_SIMPLE_NUM + 1
while num % i != 0:
    if num % 2 == 0 or num <= FIRST_SIMPLE_NUM:
        break
    i += 2
if num == i or num == FIRST_SIMPLE_NUM:
    print(f"Число {num} простое")
else:
    print(f"Число {num} составное")
