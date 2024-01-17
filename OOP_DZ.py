class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_rating(self, course):
         return round(sum(self.grades[course])/len(self.grades[course]), 1)

    def rate_lect(self, lecturer, course, grade):
        if 0 < grade <= 10:
            if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached_lect and course in self.courses_in_progress:
                if course in lecturer.lecturer_grades:
                    lecturer.lecturer_grades[course] += [grade]
                else:
                    lecturer.lecturer_grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return "Оценка вне допустимого диапозона"

    def __lt__(self, other):
        if self.average_rating(for_test) < other.average_rating(for_test):
            return f'True - Студент {self.name} {self.surname} учится хуже, чем {other.name} {other.surname}'
        else:
            return f'False - Студент {self.name} {self.surname} учится не хуже, чем {other.name} {other.surname}'

    def __gt__(self, other):
        if self.average_rating(for_test) > other.average_rating(for_test):
            return f'True - Студент {self.name} {self.surname} учится лучше, чем {other.name} {other.surname}'
        else:
            return f'False - Студент {self.name} {self.surname} учится не лучше, чем {other.name} {other.surname}'

    def __eq__(self, other):
        if self.average_rating(for_test) == other.average_rating(for_test):
            return f'True - Студенты {self.name} {self.surname} и {other.name} {other.surname} учатся одинаково'
        else:
            return f'False - Студенты {self.name} {self.surname} и {other.name} {other.surname} имеют разный средний балл за ДЗ'

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {self.average_rating(for_test)}\n" \
               f"Курсы в процессе изучения: {(', ').join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {(', ').join(self.finished_courses)}"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Курсы: {(', ').join(self.courses_in_progress)}"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached_lect = []
        self.lecturer_grades = {}

    def average_rating(self, course):
        return round(sum(self.lecturer_grades[course])/len(self.lecturer_grades[course]), 1)

    def __gt__(self, other):
        if self.average_rating(for_test) > other.average_rating(for_test):
            return f'True - Лектор {self.name} {self.surname} читает лекции лучше, чем {other.name} {other.surname}'
        else:
            return f'False - Лектор {self.name} {self.surname} читает лекции не лучше, чем {other.name} {other.surname}'

    def __eq__(self, other):
        if self.average_rating(for_test) == other.average_rating(for_test):
            return f'True - Лекторы {self.name} {self.surname} и {other.name} {other.surname} имеют одинаковый рейтинг'
        else:
            return f'False - Лекторы {self.name} {self.surname} и {other.name} {other.surname} имеют разный рейтинг'

    def __str__(self):
        return (f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname} \n" \
               f"Средняя оценка за лекции: {self.average_rating(for_test)}")


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if 0 < grade <= 10:
            if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return "Оценка вне допустимого диапозона"

    def __str__(self):
        return (f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}")


def avg_rating_all_students(students_list: list, course):
    avg_all_s = 0
    for student in students_list:
        avg_all_s += student.average_rating(course)
    return avg_all_s / len(students_list)


def avg_rating_all_lecturer(lecturers_list: list, course):
    avg_all_l = 0
    for lecturer in lecturers_list:
        avg_all_l += lecturer.average_rating(course)
    return avg_all_l / len(lecturers_list)

student1 = Student('Ruoy', 'Eman', 'm')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Jack', 'Kakoyto', 'm')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Введение в программирование']

students_list = [student1, student2]

reviewer1 = Reviewer('Egor', 'Krasnov')
reviewer1.courses_attached += ['Python']
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 10)

reviewer2 = Reviewer('Alexey', 'Lavrov')
reviewer2.courses_attached += ['Python']
reviewer2.rate_hw(student2, 'Python', 5)
reviewer2.rate_hw(student1, 'Python', 2)
reviewer2.rate_hw(student1, 'Python', 10)

lect1 = Lecturer('Pavel', 'Ivanov')
lect1.courses_attached_lect += ['Python']
student1.rate_lect(lect1, 'Python', 8)
student2.rate_lect(lect1, 'Python', 4)
student1.rate_lect(lect1, 'Python', 10)

lect2 = Lecturer('Nikita', 'Vasilev')
lect2.courses_attached_lect += ['Python']
student2.rate_lect(lect2, 'Python', 10)
student2.rate_lect(lect2, 'Python', 9)
student1.rate_lect(lect2, 'Python', 7)

lecturers_list = [lect1, lect2]

for_test = 'Python'
print(f"Студент \n{student1}\n")
print(f"Студент \n{student2}\n")
print(f"Лектор \n{lect1}\n")
print(f"Лектор \n{lect2}\n")
print(f"Проверяющий\n{reviewer1}\n")
print(f"Проверяющий\n{reviewer2}\n")

print(student1 > student2)
print(student1 == student2)
print(lect1 > lect2)
print(lect1 < lect2)

print(f'Средняя оценка всех студентов по курсу {for_test}: {avg_rating_all_students(students_list, for_test)}')
print(f'Средняя оценка всех лекторов по курсу {for_test}: {avg_rating_all_lecturer(lecturers_list, for_test)}')