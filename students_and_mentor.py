class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.gpa = 0

    def add_courses_in_progress(self, course):
        if course.name not in self.courses_in_progress:
            self.courses_in_progress.append(course.name)
            course.students[self.name] = []
        else:
            return 'Ошибка'

    def calculating_gpa(self):
        reating = []
        tmp = 0
        for i in list(self.grades.values()):
            for k in i:
                reating.append(k)
        for i in reating:
            tmp += i
        self.gpa = round((tmp / len(reating)), 1)
    
    def rate_lec(self, lector, course, grade):
        if 0 <= grade <= 10:
            if isinstance(lector, Lector) and course.name in self.courses_in_progress and course.name in lector.courses_attached:
                if course.name in lector.grades:
                    lector.grades[course.name] += [grade]
                    course.lectors[lector.name] += [grade]
                else:
                    lector.grades[course.name] = [grade]
                    course.lectors[lector.name] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Оценка только по 10-тибальной шкале'
        lector.calculating_gpa()
        course.lectors_gpa()

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (float, Student)):
            raise TypeError("Операнд справа должен иметь тип float или Student")
 
        return other if isinstance(other, float) else other.gpa

    def __eq__(self, other):
        gpa = self.__verify_data(other)
        return self.gpa == gpa

    def __lt__(self, other):
        gpa = self.__verify_data(other)
        return self.gpa < gpa

    def __le__(self, other):
        gpa = self.__verify_data(other)
        return self.gpa <= gpa

    def __str__(self):
        list_courses_in_progress = ''
        for i in self.courses_in_progress:
            list_courses_in_progress += f'{i}, '

        list_finished_courses = ''
        for i in self.finished_courses:
            list_finished_courses += f'{i}, '
        
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задание: {self.gpa}
Курсы в процессе изучения: {list_courses_in_progress}
Завершенные курсы: {list_finished_courses}
'''

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    
class Lector(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.gpa = 0

    def add_course_to_attached(self, course):
        if course.name not in self.courses_attached:
            self.courses_attached.append(course.name)
            course.lectors[self.name] = []
        else:
            return 'Ошибка'

    def calculating_gpa(self):
        reating = []
        tmp = 0
        for i in list(self.grades.values()):
            for k in i:
                reating.append(k)
        for i in reating:
            tmp += i
        self.gpa = round((tmp / len(reating)), 1)

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (float, Lector)):
            raise TypeError("Операнд справа должен иметь тип float или Lector")
 
        return other if isinstance(other, float) else other.gpa

    def __eq__(self, other):
        gpa = self.__verify_data(other)
        return self.gpa == gpa

    def __lt__(self, other):
        gpa = self.__verify_data(other)
        return self.gpa < gpa

    def __le__(self, other):
        gpa = self.__verify_data(other)
        return self.gpa <= gpa

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.gpa}
'''

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if 0 <= grade <= 10:
            if isinstance(student, Student) and course.name in self.courses_attached and course.name in student.courses_in_progress:
                if course.name in student.grades:
                    student.grades[course.name] += [grade]
                    course.students[student.name] += [grade]
                else:
                    student.grades[course.name] = [grade]
                    course.students[student.name] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Оценка только по 10-тибальной шкале'
        student.calculating_gpa()
        course.students_gpa()

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}
'''

class Course:
    def __init__(self, name):
        self.name = name
        self.students = {}
        self.lectors = {}
        self.st_gpa = 0
        self.lec_gpa = 0

    def students_gpa(self):
        reating = []
        tmp = 0
        for i in list(self.students.values()):
            for k in i:
                reating.append(k)
        for i in reating:
            tmp += i
        self.st_gpa = round((tmp / len(reating)), 1)

    def lectors_gpa(self):
        reating = []
        tmp = 0
        for i in list(self.lectors.values()):
            for k in i:
                reating.append(k)
        for i in reating:
            tmp += i
        self.lec_gpa = round((tmp / len(reating)), 1) 

    def __str__(self):
        return f'''Название курса: {self.name}
Средний балл студентов на курсе: {self.st_gpa}
Средний балл лекторов на курсе: {self.lec_gpa}
'''       
    
python = Course('Python')
git = Course('Git')

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.add_courses_in_progress(python)
best_student.finished_courses += ['Git']

maxim = Student('Maxim', 'Shakurov', 'male')
maxim.add_courses_in_progress(python)
maxim.finished_courses += ['Git']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, python, 9)
cool_mentor.rate_hw(best_student, python, 10)
cool_mentor.rate_hw(best_student, python, 10)

cool_mentor.rate_hw(maxim, python, 10)
cool_mentor.rate_hw(maxim, python, 8)
cool_mentor.rate_hw(maxim, python, 10)

oleg = Lector('Oleg', 'Bulygin')
oleg.add_course_to_attached(python)
elena = Lector('Elena', 'Nikitina')
elena.add_course_to_attached(python)

best_student.rate_lec(oleg, python, 10)
best_student.rate_lec(oleg, python, 8)
best_student.rate_lec(elena, python, 8)
best_student.rate_lec(elena, python, 6)

maxim.rate_lec(oleg, python, 9)
maxim.rate_lec(oleg, python, 9)
maxim.rate_lec(elena, python, 6)
maxim.rate_lec(elena, python, 7)






print(best_student.grades)
print(best_student)
print(oleg)
print(cool_mentor)
print(best_student == maxim)
print(best_student < maxim)
print(oleg != elena)
print(oleg > elena)
print(python)