"""
Возьмите задачу о банкомате из семинара 2.
Разбейте её на отдельные операции - функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
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
op_log = []


def operation_log(op_id, op_summ):
    op_log.append((op_id, op_summ))


def replenish(op_summ):
    global balance
    balance += op_summ
    operation_log(1, op_summ)


def withdrawal(op_summ):
    global balance
    wp = Decimal(op_summ * WITHDRAWAL_PERCENTAGE)
    if wp < MIN_PERCENTAGE:
        wp = MIN_PERCENTAGE
    elif wp > MAX_PERCENTAGE:
        wp = MIN_PERCENTAGE
    if balance < op_summ + wp:
        return False
    balance -= op_summ + wp
    operation_log(2, op_summ)
    return True


def wealth_tax():
    global balance
    if balance >= 5_000_000:
        balance -= Decimal(balance * TAX)


def check_op_mul(op_summ):
    return True if op_summ % OPERATION_MUL == 0 else False


while True:
    print(f"Остаток на счете: {balance}")
    print(operation_count)
    operation = int(input("1 Пополнить, 2 Снять, 0 Выход "))
    if operation == 0:
        break
    wealth_tax()
    summ = int(input("Сумма: "))
    if not check_op_mul(summ):
        print(f"Сумма операции должна быть кратна {OPERATION_MUL}")
        continue
    if operation == 1:
        replenish(summ)
    elif operation == 2:
        if not withdrawal(summ):
            print("Недостаток средств")
            continue
    operation_count += 1
    if operation_count % INTEREST_COUNT == 0:
        balance += Decimal(balance * INTEREST)
