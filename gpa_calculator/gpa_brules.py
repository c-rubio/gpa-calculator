grade_key = {
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'F': 0.0,
}
letterToBoolDict = {
    'Y': True,
    'N': False,
}

def letterToBool(letter):
    if ((letter == 'Y') or (letter == 'N')):
        Bool = letterToBoolDict[letter]
    return Bool

def convertToNumberGrade(letterGrade: str) -> float:
    gradePoints = grade_key[letterGrade]
    return gradePoints