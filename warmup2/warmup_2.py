from student import Student
from course import Course


def create_students(filename):
    """
    Reads a text file containíng student information, 
    and creates Student-objects based on the contents.
    Name of the file to be read is given as the parameter.
    Each correct row of the file has a name and a student number separated by a slash ('/').
    If a row is correct, a new Student-object is created with that name and student number.
    Incorrect rows, i.e. rows that do not have a string and an integer separated by a slash,
    are skipped.
    Finally, the function returns a list of all created Student-objects.
    """

    try:
        file = open(filename, 'r')
        students = []
        for line in file:
            line = line.rstrip()
            line = line.split('/')
            if len(line) == 2:
                try:
                    student = Student(line[0], int(line[1]))
                    students.append(student)
                except ValueError:
                    pass
        return students
    except OSError:
        return 'invalid file'


def add_courses(filename, student):
    """
    Reads a text file containing course information,
    creates Course-objects based on the contents, and adds them
    to the completed courses of the student given as the second parameter.
    Name of the file to be read is given as the first parameter.
    Each correct row of the file has the name of the course and its credits
    separated by a comma (','). Incorrect rows, i.e. rows that do not have a string
    and an integer separated by a comma, are skipped.
    Credits for a course should be in the range 1-15.
    Function returns the amount of courses successfully added for the student.
    """

    try:
        file = open(filename, 'r')
        for line in file:
            line = line.rstrip()
            line = line.split(',')
            if len(line) == 2 and 1 <= int(line[1]) <= 15:
                course = Course(line[0], int(line[1]))
                student.add_course(course)
        return len(student.get_courses())
    except OSError:
        return 'invalid file'


def compare_student_numbers(student1, student2):
    """
    Compares two given Student-objects, student1 and student2, and returns the one with a smaller id.

    EXAMPLE:
    given objects:
    student1, id: 123456
    student2, id: 234567

    compare_student_numbers(student1, student2):
    returns: student1
    """

    if student1.get_id() < student2.get_id():
        return student1
    else:
        return student2


def get_credits(student):
    """
    Calculates and returns the sum of credits of all the courses the student has completed.
    """

    total = 0
    for course in student.get_courses():
        total += int(course.get_credits())
    return total


def compare_credits(student1, student2):
    """
    Compares two students total credits. Returns the student with the highest credit count.
    Use the function get_credits to get the total credits. 
    If both students have an equal amount of credits, the function returns 0.
    """

    if get_credits(student1) > get_credits(student2):
        return student1
    elif get_credits(student1) < get_credits(student2):
        return student2
    else:
        return 0


def main():
    student_list = create_students('student_file.txt')

    for student in student_list:
        filename = input("Enter the name of the course file\n")
        courses = add_courses(filename, student)
        print("{:d} courses added for {:s}".format(courses, student.get_name()))

    for student in student_list:
        print("{:s} has {:d} credits".format(student.get_name(), get_credits(student)))

    more_credits = compare_credits(student_list[0], student_list[4])


if __name__ == "__main__":
    main()
