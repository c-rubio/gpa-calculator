from dataclasses import dataclass
import csv
import helpers as hp

@dataclass
class Course:
    name : str = ""
    grade : float = 0.00
    hours : float = 0.00
    is_major : bool = False
    is_retaken : bool = False
    semester: int = 0

CSV_FIELDS = ['name', 'grade', 'hours', 'is_major', 'is_retaken', 'semester']

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

def write_courses(course_dict: dict, file_name: str):

    with open(f'gpa-calculator/src/{file_name}.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames = CSV_FIELDS)
        csv_writer.writeheader()
        for course in course_dict.values():
            csv_writer.writerow(course.__dict__)

def read_courses(course_dict: dict, file_name: str):

    csv_list = []
    with open(f'gpa-calculator/src/{file_name}', 'r') as csv_file:
            csv_info = csv.DictReader(csv_file)
            for line in csv_info:
                csv_list.append(dict(line))
            for course in csv_list:
                cls = Course(**course)
                course_dict[cls.name + cls.semester] = cls
                cls.grade = float(cls.grade)
                cls.hours = float(cls.hours)
                cls.is_major = hp.convert_bool(cls.is_major, "True")
                cls.is_retaken = hp.convert_bool(cls.is_retaken, "True")
                cls.semester = int(cls.semester)
    