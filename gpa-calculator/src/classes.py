# Course class used to organize individual instances of courses and allow for
# organization into a dict data structure


import helpers as hp


class Course:
    def __init__(
            self, name: str, grade: float, hours: float,
            is_major: bool, is_duplicate: bool, semester: int) -> None:

        self.name = name
        self.grade = grade
        self.hours = hours
        self.is_major = is_major
        self.is_duplicate = is_duplicate
        self.semester = semester

    def __str__(self):
        return (f'Course Name: {self.name} Grade: {self.grade}', 
        f'Credit Hours: {self.hours} Major Course: {self.is_major}', 
        f'Duplicate Course: {self.is_duplicate}')

    def get_name(self) -> None:
        return self.name

    def get_grade(self) -> None:
        return self.grade

    def get_hours(self) -> None:
        return self.hours

    def get_is_major(self) -> None:
        return self.is_major

    def get_is_duplicate(self) -> None:
        return self.is_duplicate

    def get_semester(self) -> None:
        return self.semester

    def set_name(self, name: str) -> None:
        self.name = name

    def set_grade(self, grade: str) -> None:
        grade = hp.grade_key(grade)
        self.grade = grade

    def set_hours(self, hours: float) -> None:
        self.hours = hours

    def set_major(self, is_major: bool) -> None:
        self.is_major = is_major

    def set_duplicate(self, is_duplicate) -> None:
        self.is_duplicate = is_duplicate

    def print_course(self) -> None:
        self.get_name()
        self.get_grade()
        self.get_hours()
        self.get_is_major()
        self.get_is_duplicate()
