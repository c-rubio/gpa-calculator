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

    :param letter_grade: letter representation of a class grade
    return: float representation of the input letter grade
    """
    grade_points = grade_key[letter_grade]
    return grade_points


def validate_input(user_prompt, expected_input, expected_type):
    """
    validate_input is a general input validation function to ensure a user input
    the program's expected value. it is designed to allow the programmer to 
    dynamically choose the expected values.

    :param user_prompt: output to display in the terminal to prompt a user 
    :param expected_input: input that programmer expects
    :param expected_type: input type that programmer expects
    :return: void                                     
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
            print("Incorrect Input. Try again.",
            "Expected inputs include: ", expected_input)

def compute_gpa_factors(courses, cred_hrs: int = 0, grade_pts: int = 0):
    """
    compute_gpa_factors updates and computes the credit hours and grade points
    for a GPA calculation based upon information from iterable data structure 
    filled with Course object instances

    :param courses: iterable data structure containing Course objects
    :param cred_hrs: credit hour variable to be updated
    :param grade_pts: grade point variable to be updated
    :return: updated credit hours and grade points
    """
    if courses is None: 
        print("Invalid Call, Pass a course storage as argument.")
        return cred_hrs, grade_pts

    if len(courses) == 0:
        return cred_hrs, grade_pts

    for course in courses.values():
        cred_hrs += course.get_hours()
        grade_pts += course.get_grade() * course.get_hours()
        return cred_hrs, grade_pts

    
def convert_bool(attr, true_var) -> bool:
    """
    convert_bool converts the attr to a bool based upon whether or not it equals
    the value of the true_var parameter

    :param attr: any object
    :param true_var: any object
    :return: bool True if attr equals true_var value, False if not
    """
    if attr == true_var:
        return True
    else:
        return False