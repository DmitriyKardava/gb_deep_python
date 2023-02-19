from sys import argv


def _is_leap_year(year: int) -> bool:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


def check_date(date: str) -> bool:
    long_month = (1, 3, 7, 8, 10, 12)
    day, month, year = map(int, date.split('.'))
    if year < 0 or year > 9999:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if month not in long_month and day > 30:
        return False
    if month == 2:
        if _is_leap_year(year):
            if day > 29:
                return False
        else:
            if day > 28:
                return False
    return True


if __name__ == "__main__":
    if len(argv) > 1:
        if not check_date(argv[1]):
            print(f"Некорректная дата {argv[1]}")
            exit(-1)
