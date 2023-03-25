import csv


class Range:
    def __init__(self, min_val=None, max_val=None):
        self.min_val = min_val
        self.max_val = max_val

    def __set_name__(self, owner, name):
        self.param_name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f"Значение {value} должно быть целым числом")
        if self.min_val is not None and value < self.min_val:
            raise ValueError(f"Значение {value} должно быть больше или равно {self.min_val}")
        if self.max_val is not None and value > self.max_val:
            raise ValueError(f"Значение {value} должно быть меньше или равно {self.max_val}")
        setattr(instance, self.param_name, value)


class FIODescriptor:
    def __set_name__(self, owner, name):
        self.param_name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if not value.isalpha():
            raise ValueError('В ФИО допускаются только буквы')
        if not value.istitle():
            raise ValueError('ФИО должны начинаться с заглавной буквы')
        setattr(instance, self.param_name, value)


class SubjectDescriptor:
    def __set_name__(self, owner, name):
        self.param_name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if value[1] not in value[0]:
            raise ValueError(f"{value[1]} не в списке предметов")
        setattr(instance, self.param_name, value)


class MarkDescriptor:
    mark = Range(2, 5)
    subject = SubjectDescriptor()

    def __set_name__(self, owner, name):
        self.param_name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        marks = {}
        if value:
            self.subject = instance.subjects, value[0]
            self.mark = value[1]
            marks = instance.marks
            if marks.get(value[0]):
                marks[value[0]].append(self.mark)
            else:
                marks[value[0]] = [self.mark]
        setattr(instance, self.param_name, marks)


class TestDescriptor:
    test = Range(0, 100)
    subject = SubjectDescriptor()

    def __set_name__(self, owner, name):
        self.param_name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        tests = {}
        if value:
            self.test = value[1]
            self.subject = instance.subjects, value[0]
            tests = instance.tests
            if tests.get(value[0]):
                tests[value[0]].append(self.test)
            else:
                tests[value[0]] = [self.test]
        setattr(instance, self.param_name, tests)


class Student:
    name = FIODescriptor()
    last_name = FIODescriptor()
    patronymic = FIODescriptor()
    marks = MarkDescriptor()
    tests = TestDescriptor()

    @staticmethod
    def _load_subjects():
        with open('subjects.csv', 'r', encoding='utf-8') as f:
            data = list(csv.reader(f))
        return data[0]

    def __init__(self, last_name, name, patronymic):
        self.name = name
        self.last_name = last_name
        self.patronymic = patronymic
        self.subjects = self._load_subjects()
        self.marks = {}
        self.tests = {}

    def __str__(self):
        return f"Студент:\n" \
               f"ФИО: {self.last_name} {self.name} {self.patronymic}\n" \
               f"Предметы: {self.subjects}\n" \
               f"Оценки: {self.marks}\n" \
               f"Тесты: {self.tests}"

    def set_mark(self, subject, mark):
        self.marks = (subject, mark)

    def set_test(self, subject, test):
        self.tests = (subject, test)


if __name__ == '__main__':
    student = Student('Иванов', 'Иван', 'Иванович')
    student.set_mark('русский язык', 4)
    student.set_mark('русский язык', 5)
    student.set_test('английский язык', 99)
    student.set_mark('python', 10)

    print(student)
