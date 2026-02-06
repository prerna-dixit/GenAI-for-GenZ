class Student:
    def __init__(self, student_id, name, department):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.courses = []

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def drop(self, course):
        if course in self.courses:
            self.courses.remove(course)


class Course:
    def __init__(self, course_code, title, credits):
        self.course_code = course_code
        self.title = title
        self.credits = credits
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            student.enroll(self)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            student.drop(self)


class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self, student_id, name, department):
        self.students[student_id] = Student(student_id, name, department)

    def add_course(self, course_code, title, credits):
        self.courses[course_code] = Course(course_code, title, credits)

    def enroll_student(self, student_id, course_code):
        student = self.students.get(student_id)
        course = self.courses.get(course_code)
        if student and course:
            course.add_student(student)

    def get_student_courses(self, student_id):
        student = self.students.get(student_id)
        return student.courses if student else []
