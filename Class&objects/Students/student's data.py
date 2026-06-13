from main import students

stu1 = students("mhmd", 24, 5, "computer engineer")
stu2 = students("mostafa", 19, 0, "primary engineer")
stu3 = students("Rovan", 21, 4, "call center")
stu4 = students("amr", 18, 1, "artiest")
stu5 = students("amin", 24, 5, "business man")

team = [stu1, stu2, stu3, stu4, stu5]

for students in team:
    if students.grade == 5:
        print(students.name, students.age, students.major)

for students in team:
    if students.age < 20:
        print(students.name, students.grade, students.major)

for students in team:
    if students.major == "call center":
        print(students.name)
        break
    else:
        print("not founded")