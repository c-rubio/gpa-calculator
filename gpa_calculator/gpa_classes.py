# Course class used to organize instances of classes


import gpa_brules as br


class Course:
    def __init__(
            self, name: str, grade: float, hours: float,
            isMajor: bool, is_duplicate: bool, semester: int) -> None:

        self.name = name
        self.grade = grade
        self.hours = hours
        self.isMajor = isMajor
        self.isDuplicate = is_duplicate
        self.semester = semester

    def __str__(self):
        return (f'Course Name: {self.name} Grade: {self.grade}', 
        f'Credit Hours: {self.hours} Major Course: {self.isMajor}', 
        f'Duplicate Course: {self.isDuplicate}')

    def get_name(self) -> None:
        return self.name

    def get_grade(self) -> None:
        return self.grade

    def get_hours(self) -> None:
        return self.hours

    def get_major(self) -> None:
        return self.isMajor

    def get_duplicate(self) -> None:
        return self.isDuplicate

    def get_semester(self) -> None:
        return self.semester

    def set_name(self, name: str) -> None:
        self.name = name

    def set_grade(self, grade: str) -> None:
        grade = br.grade_key(grade)
        self.grade = grade

    def set_hours(self, hours: float) -> None:
        self.hours = hours

    def set_major(self, isMajor: bool) -> None:
        self.isMajor = isMajor

    def set_duplicate(self, isDuplicate) -> None:
        self.isDuplicate = isDuplicate

    def print_course(self) -> None:
        self.get_name()
        self.get_grade()
        self.get_hours()
        self.get_major()
        self.get_duplicate()
