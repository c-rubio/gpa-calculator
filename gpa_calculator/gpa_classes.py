import gpa_brules as br

class Course:
    def __init__(self, name: str, grade: float, hours: float, isMajor: bool, isDuplicate: bool, semester: int) -> None:
        self.name = name
        self.grade = grade
        self.hours = hours
        self.isMajor = isMajor
        self.isDuplicate = isDuplicate
        self.semester = semester
        
    def __str__(self):
        return f'{self.name} {self.grade} {self.hours} {self.isMajor} {self.isDuplicate}'

    def getName(self) -> None:
        print("Course Name: ", self.name)
    
    def getGrade(self) -> None:
        print(f"Course Name: {self.grade:.2f}")
    
    def getHours(self) -> None:
        print("Course Hours: ", self.hours)

    def getMajor(self) -> None:
        print("Major Course: ", self.isMajor)
    
    def getDuplicate(self) -> None:
        print("Duplicate Course: ", self.isDuplicate)
    
    def getSemester(self) -> None:
        print("Duplicate Course: ", self.isDuplicate)

    def setName(self, name: str) -> None:
        self.name = name

    def setGrade(self, grade: str) -> None:
        grade = br.grade_key(grade)
        self.grade = grade
    
    def setHours(self, hours: float) -> None:
        self.hours = hours

    def setMajor(self, isMajor: bool) -> None:
        self.isMajor = isMajor
    
    def setDuplicate(self, isDuplicate) -> None:
        self.isDuplicate = isDuplicate

    def printCourse(self) -> None:
        self.getName()
        self.getGrade()
        self.getHours()
        self.getMajor()
        self.getDuplicate()
        
