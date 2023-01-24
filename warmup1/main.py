import warmup


def main():

    print('names1:', warmup.names_from_file('names_1.txt'))
    print('names2:', warmup.names_from_file('names_2.txt'))
    print('error:', warmup.names_from_file('bruh.txt'))

    print("correction of string:")
    string = "a!b?c%d/ef"
    corrected_string = warmup.correct_string(string, ["%", "!", "?", "/"])
    print("{:s} to {:s}".format(string, corrected_string))

    print("Weighted average of courses is:")
    courses = [[5, "Basics in Programming Y1", 5], [2, "Communicating Technology", 3], [3, "Fourier Analysis", 5]]
    average = warmup.count_weighted_average(courses)
    print(average)

    print("Given number belongs to student:")
    dictionary = { "Tiina Teekkari" : "111111", "Teemu Teekkari": "222222", "Kaisa Kemisti": "333333", "Kalle Kemisti": "444444" }
    name = warmup.find_student(dictionary, "222222")
    print(name)

    print("These students are on both courses:")
    list1 = ["Tiina Teekkari", "Teemu Teekkari", "Kaisa Kemisti", "Kalle Kemisti"]
    list2 = ["Anni Arkkitehti", "Antti Arkkitehti", "Teemu Teekkari", "Kaisa Kemisti"]
    namelist = warmup.is_on_course(list1, list2)
    print(namelist)


main()
