python_class = ["Anil", "Bina", "Chetan", "Deepa", "Anil", "Esha"]
java_class = ["Chetan", "Farhan", "Deepa", "Gita", "Bina"]

python_students=set(python_class)
java_students=set(java_class)

print("Students enrolled in python are ",python_students)
print("Students enrolled in java are ",java_students)

Both=python_students & java_students
Only_python=python_students-java_students
Exactly_one=python_students^java_students
Unique=python_students|java_students

print("Students studying both courses are ",Both)
print("Students studying only python are ", Only_python)
print("Students studying exactly one course are ", Exactly_one)
print("Unique students in sorted order are ", sorted(Unique))

name=input("Enter name of student: ")
if name in python_students & java_students:
    print("Student is enrolled in both courses.")
elif name in python_students:
    print("Student is enrolled only in python course.")
elif name in java_students:
    print("Student is enrolled only in java course.")
else:
    print("Student is not enrolled in any course")