# generic or specific functions used in the gpa main to supplement or enhance
# the experience


grade_key = {
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'F': 0.0,
}


def letter_to_num_grade(letter_grade: str) -> float:
    """
    letter_to_num_grade converts a letter grade to a number grade according to the 
    NC A&T grade policy by finding a match in the grade_key dict

    Parameters:                                                         \n
    letter_grade -- letter representation of a class grade               \n

    Returns:                                                            \n
    grade_points -- float representation of the input letter grade
    """
    grade_points = grade_key[letter_grade]
    return grade_points


def validate_input(user_prompt, expected_input, expected_type):
    """
    validate_input is a general input validation function to ensure a user input
    the program's expected value. it is designed to allow the programmer to 
    dynamically choose the expected values.

    Parameters:                                                         \n
    user_prompt    -- output to display in the terminal to prompt a user \n
    expected_input -- input that programmer expects                      \n
    expected_type  -- input type that programmer expects                 \n

    Returns:                                                            \n
    void                                        
    """
    while True:
        user_input = input(user_prompt)
        if type is not None:
            try:
                user_input = expected_type(user_input)
            except ValueError:
                print("Improper Input Value. Try Again.")
        if user_input in expected_input:
            return user_input
        else:
            print("Incorrect Input. Try again. \
            Expected inputs include: ", expected_input)
