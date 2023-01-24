def names_from_file(filename):
    """
    Return a list of strings that are read from __filename__-file.

    PARAMETERS:
    filename (string) : name of the file to read strings from
    """
    names = []
    try:
        file = open(filename, 'r')
        for line in file:
            line = line.rstrip()
            names.append(line)
        return names
    except OSError:
        return 'invalid file'


def correct_string(string, symbols):
    """
    Return a new string which is __string__ without characters that are in __symbols__-list.
    You can assume that every item in __symbols__ are one character long.

    PARAMETERS:
    string (string) : a string of characters
    symbols (list) : a list of characters

    EXAMPLE:
    correct_string( "a!b?c%d/ef" , ["%","!","?","/"] )
    returns "abcdef".
    """
    corrected_string = ''
    for character in string:
        if character not in symbols:
            corrected_string += character
    return corrected_string


def count_weighted_average(courses):
    """
    Return a weighted average* of courses from given 2-dimensional list __courses__.
    Average is zero if there are no courses in __courses__-list.
    *Weighted average is counted: sum of grade*credits from all courses / sum of all credits

    PARAMETERS:
    courses (2-dimensional list) : A list of courses. One course is a 3 item list: [grade, coursename , credits]

    EXAMPLE:
    count_weighted_average( [[5, "Basics in Programming Y1", 5], [2, "Communicating Technology", 3],[3, "Fourier Analysis", 5]] )
    returns 3.5384615384615383
    """
    sum = 0
    creditsum = 0
    for course in courses:
        sum += course[0] * course[2]
        creditsum += course[2]
    if creditsum != 0:
        return sum / creditsum
    else:
        return 0


def find_student(dictionary, info):
    """
    Search __info__ from __dictionary__ values and returns the dictionary key of __info__.
    If __info__ is not in dictionary return False.

    PARAMETERS:
    dictionary (dictionary) : string points to 2-dimensional list
    info (2-dimensional list) : __courses__-list from count_weighted_average

    EXAMPLE:
    dictionary = { "Tiina Teekkari" : info1, "Teemu Teekkari": info2, "Kaisa Kemisti": info3 , "Kalle Kemisti": info4 }

    find_student(dictionary, info2)
    returns "Teemu Teekkari"
    """
    try:
        value = list(dictionary.keys())[list(dictionary.values()).index(info)]
        return value
    except ValueError:
        return False


def is_on_course(students, participants):
    """
    Return a list of strings that are on both __students__-list and __participants__list, and the length of the new list.

    PARAMETERS:
    students (list) : list of strings
    participants (list) : list of strings

    RETURNS:
    a list, a length of the list (int)

    EXAMPLE:
    students = ["Tiina Teekkari", "Teemu Teekkari", "Kaisa Kemisti", "Kalle Kemisti"]
    participants = ["Anni Arkkitehti", "Antti Arkkitehti", "Teemu Teekkari", "Kaisa Kemisti"]

    is_on_course(students,participants)
    returns ["Teemu Teekkari", "Kaisa Kemisti"], 2
    """
    on_course = []
    for student in students:
        if student in participants:
            on_course.append(student)
    return on_course, len(on_course)
