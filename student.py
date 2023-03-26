import csv
from errors import RangeError, NotIntError, NotAlphaError, NotTitleError, WrongSubjectError


class Range:
    def __init__(self, min_val=None, max_val=None):
        self.min_val = min_val
        self.max_val = max_val

    def __set_name__(self, owner, name):
        self.param_name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if value:
            if not isinstance(value, int):
                raise NotIntError(value)
            if self.min_val is not None and value < self.min_val:
                raise RangeError(value, self.min_val, self.max_val)
            if self.max_val is not None and value > self.max_val:
                raise RangeError(value, self.min_val, self.max_val)
            setattr(instance, self.param_name, value)


class FIODescriptor:
    def __set_name__(self, owner, name):
        self.param_name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if not value.isalpha():
            raise NotAlphaError(value)
        if not value.istitle():
            raise NotTitleError(value)
        setattr(instance, self.param_name, value)


class SubjectDescriptor:
    def __init__(self):
        self.subjects = {}

    def __set_name__(self, owner, name):
        self.param_name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if value:
            if value[1] not in value[0]:
                raise WrongSubjectError(value[1])
            setattr(instance, self.param_name, value)


class MarkDescriptor:
    mark = Range(2, 5)
    subject = SubjectDescriptor()

    @staticmethod
    def _set_mark(subject, marks, mark):
        if marks.get(subject):
            marks[subject].append(mark)
        else:
            marks[subject] = [mark]

    def __init__(self, mark=None, subject=None):
        self.mark = mark
        self.subject = subject

    def __set_name__(self, owner, name):
        self.param_name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if value:
            self.subject = instance.subjects, value['subject']
            self.mark = value['mark']
            self._set_mark(value['subject'], instance.marks, self.mark)
        else:
            setattr(instance, self.param_name, {})


class TestDescriptor(MarkDescriptor):
    test = Range(0, 100)
    subject = SubjectDescriptor()

    def __init__(self, test=None, subject=None):
        self.test = test
        self.subject = subject
        super(TestDescriptor, self).__init__()

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set_name__(self, owner, name):
        self.param_name = f"_{name}"

    def __set__(self, instance, value):
        if value:
            self.subject = instance.subjects, value['subject']
            self.test = value['mark']
            self._set_mark(value['subject'], instance.tests, value['mark'])
        else:
            setattr(instance, self.param_name, {})


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
        return f"Студент: {self.last_name} {self.name} {self.patronymic}\n" \
               f"Предметы: {self.subjects}\n" \
               f"Средний балл по тестам: {student.avg_test()}\n" \
               f"Средний балл по предметам: {student.overall_avg_score():.2f}"

    def set_mark(self, subject, mark):
        self.marks = {'subject': subject, 'mark': mark}

    def set_test(self, subject, mark):
        self.tests = {'subject': subject, 'mark': mark}

    @staticmethod
    def _average(data):
        result = {}
        for k, v in data.items():
            try:
                avg = sum(v) / len(v)
            except ZeroDivisionError:
                avg = 0
            result[k] = avg
        return result

    def avg_mark(self):
        return self._average(self.marks)

    def avg_test(self):
        return self._average(self.tests)

    def overall_avg_score(self):
        summ = 0
        count = 0
        for k, v in self.marks.items():
            summ += sum(v)
            count += len(v)
        try:
            return summ / count
        except ZeroDivisionError:
            return 0


if __name__ == '__main__':
    student = Student('Иванов', 'Иван', 'Иванович')
    student.set_mark('русский язык', 5)
    student.set_mark('русский язык', 5)
    student.set_mark('физика', 5)
    student.set_test('английский язык', 99)
    # student.set_mark('python', 10)

    print(student)
