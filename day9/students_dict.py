student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades
for score in student_scores:
    if student_scores[score] > 90:
        student_grades[score] = "Outstanding"
    elif student_scores[score] >80:
        student_grades[score] = "Exceeds Expectation"
    elif student_scores[score] > 70:
        student_grades[score] = "Acceptable"
    else:
        student_grades[score] = "Fail"

print(student_grades)

