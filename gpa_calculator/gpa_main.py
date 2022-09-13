# Basic GPA calculator using Object-Oriented Programming. No use of GUI at the moment. 
# FIXME Program not operational 
import gpa_classes
import gpa_brules as br

mainCourses = {}
archivedCourses = []

semesterCount = 1
courseNum = 0
print("Hello!")
print("Welcome to Christian's GPA Calculator")

while(True):
    while(True):
        courseName = input("Enter Course Name: ")
        courseGrade = input("Enter Course Letter Grade: ")
        courseGrade = br.convertToNumberGrade(courseGrade)
        courseHours = input("Enter Course Credit Hours: ")
        courseIsMajor = input("Is this course a major course? Y or N: ")
        courseIsMajor = br.letterToBool(courseIsMajor)

        while type(courseIsMajor) != bool:
            print("Wrong Input Type")
            courseIsMajor = input("Is this course a major course? Y or N: ")
            courseIsMajor = br.letterToBool(courseIsMajor)

        courseIsDuplicate = input("Is this a duplicate course? Y or N: ")
        courseIsDuplicate = br.letterToBool(courseIsDuplicate)
        
        while type(courseIsDuplicate) != bool:
            print("Wrong Input Type")
            courseIsDuplicate = br.letterToBool(courseIsDuplicate)

        mainCourses[courseName] = gpa_classes.Course(courseName, courseGrade, courseHours, courseIsMajor, courseIsDuplicate, semesterCount)
        continueCourse = input("Would you like to continue entering courses for semester {semesterCount}? N to cancel, any other key to continue: ")
        if continueCourse == 'N':
            break
    semesterCount += 1
    continueSemester = input("Would you like to continue semester? Y or N: ")
    if continueSemester == 'N':
        break
    
for course in mainCourses.values():
    print(course)
