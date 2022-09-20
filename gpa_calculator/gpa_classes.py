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
        return f'Course Name: {self.name} Grade: {self.grade} Credit Hours: {self.hours} Major Course: {self.isMajor} Duplicate Course: {self.isDuplicate}'

    def getName(self) -> None:
        return self.name
    
    def getGrade(self) -> None:
        return self.grade
    
    def getHours(self) -> None:
        return self.hours

    def getMajor(self) -> None:
        return self.isMajor
    
    def getDuplicate(self) -> None:
        return self.isDuplicate
    
    def getSemester(self) -> None:
        return self.semester

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
        
