from dataclasses import dataclass

@dataclass
class Course:
    name : str = "comp"
    grade : float = 4.00
    hours : float = 3.00
    is_major : bool = False
    is_duplicate : bool = False
    semester: int = "0"

def compute_gpa_factors(courses, cred_hrs: int = 0, grade_pts: int = 0):
    """
    compute_gpa_factors updates and computes the credit hours and grade 
    points for a GPA calculation based upon information from iterable data 
    structure filled with Course object instances 
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
        cred_hrs += course.hours 
        grade_pts += course.grade * course.hours
    return cred_hrs, grade_pts 