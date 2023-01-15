# Basic GPA calculator based upon NC A&T policies using Object-Oriented Programming.

import gpa_classes
import gpa_brules as br

mainCourses = {}
archivedCourses = {}


# variable initialization
semesterCount = 1
courseNum = 0
totalCredHrs = 0
totalGradePts = 0
honorsCredHrs = 0
honorsGradePts = 0
majorCredHrs = 0
majorGradePts = 0

print("Hello,")
print("Welcome to the basic GPA Calculator")

while True:
    while True:
        courseName = input("Enter Course Name: ").upper()
        courseGrade = input("Enter Course Letter Grade: ").upper()
        courseGrade = br.convertToNumGrade(courseGrade)

        courseHours = int(input("Enter Course Credit Hours: "))
        courseIsMajor = br.validateInput("Is this course a major course? Y or N: ", ["Y", "N"], str)
        courseIsDuplicate = br.validateInput("Is this course a duplicate course? Y or N: ", ["Y", "N"], str)

        if courseIsDuplicate == "Y":
            archivedCourses[courseName] = mainCourses[courseName]
            del mainCourses[courseName]
            currCourse = gpa_classes.Course(courseName, courseGrade, courseHours, courseIsMajor, courseIsDuplicate, semesterCount)
            mainCourses[currCourse.getName()] = currCourse
        else: 
            currCourse = gpa_classes.Course(courseName, courseGrade, courseHours, courseIsMajor, courseIsDuplicate, semesterCount)
            mainCourses[currCourse.getName()] = currCourse

        contSemester = br.validateInput("Would you like to continue entering courses for this semester? Y or N: ", ["Y", "N"], str)
        if contSemester == 'N':
            break

    semesterCount += 1
    contTranscript = br.validateInput("Would you like to continue to next semester? Y or N: ", ["Y", "N"], str)
    if contTranscript == 'N':
        break

for course in mainCourses.values():
    if course.getDuplicate() == "Y":
        honorsCredHrs += course.getHours()
        honorsGradePts += course.getGrade() * course.getHours()
        continue
    if course.getMajor() == "Y":
        majorCredHrs += course.getHours()
        majorGradePts  += course.getGrade() * course.getHours()

    totalCredHrs += course.getHours()
    totalGradePts += course.getGrade() * course.getHours()

if majorCredHrs != 0:
    majorGPA = majorGradePts / majorCredHrs
else:
    majorGPA = 0
    print("Major GPA can not be computed, as no major credit hours have been attempted.")
    
if honorsCredHrs != 0:
    honorsGPA = honorsGradePts / honorsCredHrs
else:
    honorsGPA = 0
    print("Honors GPA can not be computed, as no honors credit hours have been attempted.")

if totalCredHrs != 0:
    GPA = totalGradePts / totalCredHrs
else:
    GPA = 0
    print("Primary GPA can not be computed. No credit hours attempted.")

print(f"Major GPA: {majorGPA}")
print(f"Honors GPA: {honorsGPA}")
print(f"Primary GPA: {GPA}")

