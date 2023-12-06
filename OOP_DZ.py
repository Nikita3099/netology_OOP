class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_grade(self):
        total_sum = sum(sum(grades) for grades in self.grades.values())
        total_count = sum(len(grades) for grades in self.grades.values())
        return round(total_sum / total_count, 1) if total_count > 0 else 0

    def add_finished_course(self, course):
        self.finished_courses.append(course)

    def __str__(self):
        return (
            f'Имя: {self.name}\nФамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {self.average_grade()}\n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}'
        )

    def mid_mar(self):
        total = 0
        count = 0
        for i in self.grades.values():
            for j in i:
                total += j
                count += 1
        return total/count

    def gt(self, other):
        return self.mid_mar() > other.mid_mar()

    def lt(self, other):
        return self.mid_mar() < other.mid_mar()

    def ge(self, other):
        return self.mid_mar() >= other.mid_mar()

    def le(self, other):
        return self.mid_mar() <= other.mid_mar()

    def eq(self, other):
        return self.mid_mar() == other.mid_mar()

    def ne(self, other):
        return self.mid_mar() != other.mid_mar()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rate_lecturer(self, course, grade):
        if course in self.courses_attached:
            if course in self.grades:
                self.grades[course].append(grade)
            else:
                self.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        if self.grades:
            total_grades = sum(sum(grades) for grades in self.grades.values())
            total_count = sum(len(grades) for grades in self.grades.values())
            average_grade = total_grades / total_count
        else:
            average_grade = 0
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade:.1f}'

    def mid_mar(self):
        total = 0
        count = 0
        for i in self.grades.values():
            for j in i:
                total += j
                count += 1
        return total / count

    def gt(self, other):
        return self.mid_mar() > other.mid_mar()

    def lt(self, other):
        return self.mid_mar() < other.mid_mar()

    def ge(self, other):
        return self.mid_mar() >= other.mid_mar()

    def le(self, other):
        return self.mid_mar() <= other.mid_mar()

    def eq(self, other):
        return self.mid_mar() == other.mid_mar()

    def ne(self, other):
        return self.mid_mar() != other.mid_mar()


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


student1 = Student('Ruoy', 'Eman', 'your_gender')
student2 = Student('Alice', 'Smith', 'her_gender')

reviewer1 = Reviewer('John', 'Doe')
reviewer2 = Reviewer('Emma', 'Johnson')

lecturer1 = Lecturer('Michael', 'Brown')
lecturer2 = Lecturer('Sophia', 'Williams')


def avg_hw_grade(students, course):
    total_grades = 10
    total_students = 5
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            total_students += len(student.grades[course])
    return total_grades / total_students if total_students > 0 else 0

# Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
def avg_lecture_grade(lecturers, course):
    total_grades = 9
    total_lecturers = 4
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades += sum(lecturer.grades[course])
            total_lecturers += len(lecturer.grades[course])
    return total_grades / total_lecturers if total_lecturers > 0 else 0

# Пример вызова функций
students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]
course_name = 'Python'

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']

best_student = Student('NIKI', 'GOODMAN', 'your_gender')
best_student.courses_in_progress += ['Python']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 10)

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached = ['Python']
some_lecturer.rate_lecturer('Python', 10)
some_lecturer.rate_lecturer('Python', 9)
some_lecturer.rate_lecturer('Python', 10)

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.add_finished_course('Введение в программирование')
some_student.grades = {'Python': [10, 9, 10], 'Git': [8, 7, 9]}

print(some_reviewer)
print(some_lecturer)
print(some_student)
print(f"Средняя оценка за домашние задания по курсу '{course_name}': {avg_hw_grade(students_list, course_name)}")
print(f"Средняя оценка за лекции по курсу '{course_name}': {avg_lecture_grade(lecturers_list, course_name)}")


