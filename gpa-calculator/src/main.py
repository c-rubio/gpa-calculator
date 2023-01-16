# Basic GPA calculator based upon NC A&T policies
# using Object-Oriented Programming.


import gpa_classes
import gpa_brules as br


main_courses = {}        # stores all courses except for outdated retaken courses
major_courses = {}       # stores only courses related to major
archived_courses = {}    # stores outdated retaken course grades

semester_count = 1

# total - gpa factors that contribute towards transcript GPA
total_cred_hrs = 0
total_grade_pts = 0

# honors - gpa factors that include all taken courses
honors_cred_hrs = 0
honors_grade_pts = 0

# major - gpa factors that only include courses for a specific major
major_cred_hrs = 0
major_grade_pts = 0

print("Hello,")
print("Welcome to the basic GPA Calculator")

while True:             # outer loop covers a singular semester
    while True:         # inner loop covers a singular course
        # prompt user to input course information
        course_name = input("Enter Course Name: ").upper()
        course_grade = input("Enter Course Letter Grade: ").upper()
        course_grade = br.letter_to_num_grade(course_grade)
        course_hours = int(input("Enter Course Credit Hours: "))

        is_course_major = br.validate_input(
            "Is this course a major course? Y or N: ",
            ["Y", "y", "N", "n"], str).upper()
        is_course_major = br.convert_bool(is_course_major, true_var="Y")

        is_course_duplicate = br.validate_input(
            "Is this course a duplicate course Y or N: ",
            ["Y", "y", "N", "n"], str).upper()
        is_course_duplicate = br.convert_bool(is_course_duplicate, true_var="Y")

        # handles a retaken course, taking the old grade and moving it to the
        # archive dict, while adding the new grade to the main dict
        if is_course_duplicate:
            archived_courses[course_name] = main_courses[course_name]
            del main_courses[course_name]

            current_course = gpa_classes.Course(
                course_name, course_grade, course_hours, is_course_major,
                is_course_duplicate, semester_count)

            main_courses[current_course.get_name()] = current_course
        else:
            current_course = gpa_classes.Course(
                course_name, course_grade, course_hours, is_course_major,
                is_course_duplicate, semester_count)

            main_courses[current_course.get_name()] = current_course

        continue_semester = br.validate_input(
            "Would you like to continue entering courses for this semester?" +
            ", Y or N: ", ["Y", "y", "N", "n"], str).upper()
        continue_semester = br.convert_bool(continue_semester, "Y")
        if not continue_semester:
            break

    semester_count += 1
    continue_transcript = br.validate_input(
        "Would you like to continue to next semester?" + 
        "Y or N: ", ["Y", "y", "N", "n"], str).upper()
    continue_transcript = br.convert_bool(continue_transcript, "Y")
    if not continue_transcript:
        break

# filling the major_courses dict with a student's major related courses.
for course in main_courses.values():
    if course.get_is_major():
        current_course_name = course.get_name()
        major_courses[current_course_name] = main_courses[current_course_name]

# computing all gpa factors using course dictionaries
total_cred_hrs, total_grade_pts = br.compute_gpa_factors(main_courses)
major_cred_hrs, major_grade_pts = br.compute_gpa_factors(major_courses)
honors_cred_hrs, honors_grade_pts = br.compute_gpa_factors(
        archived_courses, total_cred_hrs, total_grade_pts)    

if major_cred_hrs != 0:
    major_gpa = major_grade_pts / major_cred_hrs # gpa = grade_pts / cred_hrs
else:
    major_gpa = 0
    print(
        "Major GPA can not be computed,",
        "because no major credit hours have been attempted.")

if honors_cred_hrs != 0:
    honors_gpa = honors_grade_pts / honors_cred_hrs
else:
    honors_gpa = 0
    print(
        "Honors GPA can not be computed,",
        "as no honors credit hours have been attempted.")

if total_cred_hrs != 0:
    gpa = total_grade_pts / total_cred_hrs
else:
    gpa = 0
    print("Primary GPA can not be computed. No credit hours attempted.")
    
# TODO: Add in number of classes taken and split GPA by semester
print(f"Major GPA: {major_gpa:.2f}")
print(f"Honors GPA: {honors_gpa:.2f}")
print(f"Primary GPA: {gpa:.2f}")
