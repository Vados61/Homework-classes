class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.gpa = 0

    def calculating_gpa(self):
        reating = []
        tmp = 0
        for i in list(self.grades.values()):
            for k in i:
                reating.append(k)
        for i in reating:
            tmp += i
        self.gpa = round((tmp / len(reating)), 1)
    
    def rate_lec(self,lector, course, grade):
        if 0 <= grade <= 10:
            if isinstance(lector, Lector) and course in self.courses_in_progress and course in lector.courses_attached:
                if course in lector.grades:
                    lector.grades[course] += [grade]
                else:
                    lector.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Оценка только по 10-тибальной шкале'
        lector.calculating_gpa()

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
            if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Оценка только по 10-тибальной шкале'
        student.calculating_gpa()

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}
'''

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Git']

maxim = Student('Maxim', 'Shakurov', 'male')
maxim.courses_in_progress += ['Python']
maxim.finished_courses += ['Git']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 8)
cool_mentor.rate_hw(best_student, 'Python', 10)

oleg = Lector('Oleg', 'Bulygin')
oleg.courses_attached += ['Python']
elena = Lector('Elena', 'Nikitina')
elena.courses_attached += ['Python']

best_student.rate_lec(oleg, 'Python', 10)
best_student.rate_lec(oleg, 'Python', 8)
best_student.rate_lec(elena, 'Python', 8)
best_student.rate_lec(elena, 'Python', 6)

maxim.rate_lec(oleg, 'Python', 9)
maxim.rate_lec(oleg, 'Python', 9)
maxim.rate_lec(elena, 'Python', 6)
maxim.rate_lec(elena, 'Python', 7)






#print(best_student.grades)
# print(best_student)
# print(oleg)
# print(cool_mentor)
# print(best_student == maxim)
# print(best_student < maxim)
# print(oleg != elena)
# print(oleg > elena)