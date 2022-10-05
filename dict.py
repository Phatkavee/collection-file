# Homework-02 GPA Calculator
#
# Formular GPA = sum(GradeLevel * Grade Point) / Total Credit
# Grade Point: A = 4, B = 3, C = 2, D = 1, F = 0
# Credit: Math = 3, English = 2, Science = 3, History = 2, Art = 1
# Grade Level: A = 90, B = 80, C = 70, D = 60, F = 0

Credits = {"Computer Programming": 3, "Math": 3, "English": 3, "Physic": 3, "Dance": 1, "Electronic": 3}
Grade_Level = {"A": 80, "B": 70, "C": 60, "D": 50, "F": 0}
Grade_Point = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}

Students_Marks = {"John": {"Computer Programming": 80, "Math": 90, "English": 70, "Physic": 50, "Dance": 60, "Electronic": 80}, 
                   "Peter": {"Computer Programming": 85, "Math": 80, "English": 65, "Physic": 60, "Dance": 90, "Electronic": 95}, 
                   "Mary": {"Computer Programming": 45, "Math": 70, "English": 60, "Physic": 65, "Dance": 80, "Electronic": 70},
                   "Tom": {"Computer Programming": 80, "Math": 55, "English": 75, "Physic": 70, "Dance": 75, "Electronic": 80},
                   "Jane": {"Computer Programming": 90, "Math": 95, "English": 80, "Physic": 75, "Dance": 80, "Electronic": 85}}
