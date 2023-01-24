class Student:

    def __init__(self, name, student_id):
        self.__name = name  # string
        self.__id = student_id  # integer
        self.__courses = []

    def add_course(self, course):
        self.__courses.append(course)

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_courses(self):
        return self.__courses
