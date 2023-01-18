# Basic GPA calculator based upon NC A&T policies
# using Object-Oriented Programming.


import src.classes as classes
import src.helpers as hp
import src.splash as splash

transcript_courses = {}  # stores all courses except for outdated retaken courses
major_courses = {}       # stores only courses related to major
archived_courses = {}    # stores outdated retaken course grades

semester_count = 1
user_menu_input = False

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
user_menu_input = hp.validate_input(
    "\n\nMENU: \n 1. Start New Transcript\n 2. Load .csv transcripts" +
    "\n 3. Exit \nEnter Selection: ",
     [1, 2, 3], int)

if user_menu_input == 3:
    print("\nGoodbye!")
    quit()

if user_menu_input == 2:
    transcript_file = input("\nEnter transcript courses file name: ")
    classes.read_courses(transcript_courses, transcript_file)
    stop = False
    for id in transcript_courses.keys():
        for name, course_info in transcript_courses.items():
            #TODO: Make retake detection a function
            if (transcript_courses[id].name == course_info.name) and (
                transcript_courses[id].semester != course_info.semester):
                print("RETAKEN COURSE DETECTED")
                is_course_retaken = True
                archived_courses[id] = transcript_courses[id]
                del transcript_courses[id]
                stop = True
                break
        if stop is True: break

while user_menu_input == 1:            # outer loop covers a semester(s)
    while True:                        # inner loop covers a singular course
        # prompt user to input course information
        course_name = input("\nEnter Course Name: ").upper()
        course_grade = input("Enter Course Letter Grade: ").upper()
        course_grade = hp.letter_to_num_grade(course_grade)
        course_hours = float(input("Enter Course Credit Hours: "))

        is_course_major = hp.validate_input(
            "Is this course a major course? Y or N: ",
            ["Y", "y", "N", "n"], str).upper()
        is_course_major = hp.convert_bool(is_course_major, true_var="Y")

        is_course_retaken = False
        # Detects if a course is retaken based upon repeated names in separate 
        # semesters.
        if semester_count > 1:
            for name, course_info in transcript_courses.items():
                #TODO: Make retake detection a function
                if course_name == name and semester_count != course_info.semester:
                    print("RETAKEN COURSE DETECTED, Archiving Lowest Course")
                    is_course_retaken = True
                    archived_courses[course_name] = transcript_courses[name]
                    del transcript_courses[name]
                    break
         
        current_course = classes.Course(
        course_name, course_grade, course_hours, is_course_major,
        is_course_retaken, semester_count)
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
for id, course in transcript_courses.items():
    if course.is_major:
        major_courses[id] = transcript_courses[id]

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

store_transcript = hp.validate_input(
"\nWould you like to store your current transcript?" +
" Y or N: ", ["Y", "y", "N", "n"], str).upper()
store_transcript = hp.convert_bool(store_transcript, "Y")

if store_transcript:
    transcript_file = input("\nEnter transcript courses file name (e.g. 'courses'): ")
    transcript_courses.update(archived_courses)
    classes.write_courses(transcript_courses, transcript_file)
    print(f"File saved as {transcript_file}.csv in src folder.")
