# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.
# this code was edited by Jordan on 2/8/2020

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))

exam_3 = int(input("Input exam grade three: "))
# for this list use [] and not paranthesis
# separate each with a comma..... the addition takes place is sum = sum + grade
grades = (exam_one + exam_two + exam_3)
sum = 0
# for grade in grades:
for grades in grades:
# sum = sum + grade
  sum = sum , grades
# avg = sum / len(grades)
avg = grades/3

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 70 and avg < 80:
    letter_grade = "C"
elif avg >= 60 and avg <= 70:
    letter_grade = "D"
#this should be else:  since it is the last condition and no need for comparing avg any more.
elif avg >= 50 and avg <= 59:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))
#the last two prints are not part of the loop -- remove indentation
    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter-grade == "F":
    print ("Student is failing.")
else:
    print ("Student is passing.")
