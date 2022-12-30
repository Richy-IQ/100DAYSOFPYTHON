#!/usr/bin/python3

student_heights = input("input a list of student heights\n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
total_height = 0
for height in student_heights:
    total_height += height
    #print(total_height)
number_of_students = 0
for students in student_heights:
    number_of_students += 1
    #print(number_of_students)
average_height = round(total_height / number_of_students)
print(f"the average height of the student is {average_height}")

