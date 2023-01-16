# Basic GPA calculator based upon NC A&T policies
# using Object-Oriented Programming.


import classes
import helpers as hp
import splash

transcript_courses = {}        # stores all courses except for outdated retaken courses
major_courses = {}       # stores only courses related to major
archived_courses = {}    # stores outdated retaken course grades

semester_count = 1
start = False

# total - gpa factors that contribute towards transcript GPA
transcript_cred_hrs = 0
transcript_grade_pts = 0

# honors - gpa factors that include all taken courses
honors_cred_hrs = 0
honors_grade_pts = 0

# major - gpa factors that only include courses for a specific major
major_cred_hrs = 0
major_grade_pts = 0

# splash screen
print()
splash.print_name()
splash.print_title()

# user is prompted to confirm program start, else the program is ended.
start = hp.validate_input(
    "\n\nEnter Y to start, N to exit: ", ["Y", "y", "N", "n"], str).upper()
start = hp.convert_bool(start, true_var="Y")
if not start:
    print("\nGoodbye!")
    quit()

while start:            # outer loop covers a semester(s)
    while True:         # inner loop covers a singular course
        # prompt user to input course information
        course_name = input("\nEnter Course Name: ").upper()
        course_grade = input("Enter Course Letter Grade: ").upper()
        course_grade = hp.letter_to_num_grade(course_grade)
        course_hours = float(input("Enter Course Credit Hours: "))

        is_course_major = hp.validate_input(
            "Is this course a major course? Y or N: ",
            ["Y", "y", "N", "n"], str).upper()
        is_course_major = hp.convert_bool(is_course_major, true_var="Y")
        is_course_duplicate = False

        if semester_count > 1:
            for name, course_info in transcript_courses.items():
                if course_name == name and semester_count != course_info.semester:
                    print("DUPLICATE COURSE DETECTED")
                    is_course_duplicate = True
                    archived_courses[course_name] = transcript_courses[name]
                    del transcript_courses[name]
                    break
         
        current_course = classes.Course(
        course_name, course_grade, course_hours, is_course_major,
        is_course_duplicate, semester_count)
        transcript_courses[current_course.name] = current_course

        continue_semester = hp.validate_input(
        "\nWould you like to continue entering courses for this semester?" +
        " Y or N: ", ["Y", "y", "N", "n"], str).upper()
        continue_semester = hp.convert_bool(continue_semester, "Y")
        if not continue_semester:
            break

    semester_count += 1
    continue_transcript = hp.validate_input(
        "\nWould you like to continue to next semester?" + 
        " Y or N: ", ["Y", "y", "N", "n"], str).upper()
    continue_transcript = hp.convert_bool(continue_transcript, "Y")
    if not continue_transcript:
        break

# filling the major_courses dict with a student's major related courses.
for course in transcript_courses.values():
    if course.is_major:
        major_courses[course.name] = transcript_courses[course.name]

# computing all gpa factors using course dictionaries
transcript_cred_hrs, transcript_grade_pts = classes.compute_gpa_factors(transcript_courses)
major_cred_hrs, major_grade_pts = classes.compute_gpa_factors(major_courses)
honors_cred_hrs, honors_grade_pts = classes.compute_gpa_factors(
        archived_courses, transcript_cred_hrs, transcript_grade_pts)    

# TODO: change gpa computation blocks to functions
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

if transcript_cred_hrs != 0:
    gpa = transcript_grade_pts / transcript_cred_hrs
else:
    gpa = 0
    print("Primary GPA can not be computed. No credit hours attempted.")
    
# TODO: Add in number of classes taken and split GPA by semester
print(f"\nTranscript GPA: {gpa:.2f}")
print(f"Honors GPA: {honors_gpa:.2f}")
print(f"Major GPA: {major_gpa:.2f}")
