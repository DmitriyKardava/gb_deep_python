"""
Напишите программу банкомат.
📌 Начальная сумма равна нулю
📌 Допустимые действия: пополнить, снять, выйти
📌 Сумма пополнения и снятия кратны 50 у.е.
📌 Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
📌 После каждой третей операции пополнения или снятия начисляются проценты - 3%
📌 Нельзя снять больше, чем на счёте
📌 При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
📌 Любое действие выводит сумму денег
"""
from decimal import Decimal

TAX = Decimal(0.1)
INTEREST = Decimal(0.03)
INTEREST_COUNT = 3
OPERATION_MUL = 50
WITHDRAWAL_PERCENTAGE = Decimal(0.015)
MIN_PERCENTAGE = 30
MAX_PERCENTAGE = 600
balance = Decimal(0)
operation_count = 0
while True:
    print(f"Остаток на счете: {balance}")
    print(operation_count)
    operation = int(input("1 Пополнить, 2 Снять, 0 Выход "))
    if operation == 0:
        break
    if balance >= 5_000_000:
        balance -= Decimal(balance * TAX)
    summ = int(input("Сумма: "))
    if summ % OPERATION_MUL != 0:
        print(f"Сумма операции должна быть кратна {OPERATION_MUL}")
        continue
    if operation == 1:
        balance += summ
    elif operation == 2:
        wp = Decimal(summ * WITHDRAWAL_PERCENTAGE)
        if wp < MIN_PERCENTAGE:
            wp = MIN_PERCENTAGE
        elif wp > MAX_PERCENTAGE:
            wp = MIN_PERCENTAGE
        if balance < summ + wp:
            print("Недостаток средств")
            continue
        balance -= summ + wp
    operation_count += 1
    if operation_count % INTEREST_COUNT == 0:
        balance += Decimal(balance * INTEREST)
