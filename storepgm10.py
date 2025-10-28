student = {"name": "Ayra Zainab", "roll_number": "05", "register_number": "CHAWSEL005", "department": "Computer Science", "semester": 1}
print(student)
total_mark = int(input("Enter total mark of the student: "))
student.update({"total_mark": total_mark})
mark = student["total_mark"]
if mark >= 90:
    grade = "A"
elif mark >= 82:
    grade = "B"
elif mark >= 75:
    grade = "C"
elif mark >= 60:
    grade = "D"
elif mark >= 50:
    grade = "P"
else:
    grade = "F"
student.update({"grade": grade})
print(student)
del student["roll_number"]
print(student)
