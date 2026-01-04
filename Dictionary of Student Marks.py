
student_marks = {
    "Karan": 85,
    "Amit": 78,
    "Neha": 92,
    "Riya": 88
}


name = input("Enter the student name: ")


if name in student_marks:
    print(f"Marks of {name}: {student_marks[name]}")
else:
    print("Student not found in the records.")
