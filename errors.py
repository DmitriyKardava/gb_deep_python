class StudentError(Exception):
    pass


class NotIntError(StudentError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Значение {self.value} должно быть типа int, передано {type(self.value)}."


class RangeError(StudentError):
    def __init__(self, value, min_val, max_val):
        self.value = value
        self.min = min_val
        self.max = max_val

    def __str__(self):
        return f"Значение {self.value} должно быть в диапазоне от {self.min} до {self.max}."


class FIOError(StudentError):
    pass


class NotAlphaError(StudentError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"В имени студента {self.value} допускаются только буквы."


class NotTitleError(StudentError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Первая буква в имени студента {self.value} должна быть заглавной."


class WrongSubjectError(StudentError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Предмета {self.value} нет в списке предметов изучаемых студентом."
