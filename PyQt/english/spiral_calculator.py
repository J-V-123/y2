def calculate_coordinates(line_length, amount_of_iterations, ratio):
    original_length = line_length
    amount_of_iterations = amount_of_iterations

    # these values are used from the second line forward
    x_coordinate = original_length
    y_coordinate = original_length / ratio

    # insert manually coordinates of the first two lines
    # a new line is created like this: new_line(x starting point, y starting point, x ending point, y ending point)
    coordinates = [[0, 0, original_length, 0], [original_length, 0, original_length, y_coordinate]]
    # previous coordinates are important because we are using them when we are calculating the next coordinates
    previous_coordinates = [original_length, y_coordinate]
    # set the length of the line of the current length of the line, that is currently the same as the y_coordinate
    length_of_line = y_coordinate

    new_coordinates = []
    case = 'x'
    more_specific_case_x = 'closing'
    more_specific_case_y = 'closing'

    # i is two because we already inserted first two lines in to the coordinates list
    i = 2
    while i < amount_of_iterations:
        length_of_line = length_of_line / ratio
        if case == 'x':
            if more_specific_case_x == 'closing':
                x_coordinate -= length_of_line
                more_specific_case_x = 'away'
            elif more_specific_case_x == 'away':
                x_coordinate += length_of_line
                more_specific_case_x = 'closing'

            new_coordinates = [previous_coordinates[0], previous_coordinates[1], x_coordinate, previous_coordinates[1]]
            previous_coordinates = [x_coordinate, previous_coordinates[1]]

        elif case == 'y':
            if more_specific_case_y == 'closing':
                y_coordinate -= length_of_line
                more_specific_case_y = 'away'
            elif more_specific_case_y == 'away':
                y_coordinate += length_of_line
                more_specific_case_y = 'closing'

            new_coordinates = [previous_coordinates[0], previous_coordinates[1], previous_coordinates[0], y_coordinate]
            previous_coordinates = [previous_coordinates[0], y_coordinate]

        if case == 'x':
            case = 'y'
        else:
            case = 'x'

        coordinates.append(new_coordinates)

        i += 1

    return coordinates