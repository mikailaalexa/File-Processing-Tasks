#Task 1 - read first line
file = open("students.txt", "r")

name = file.readline()

print(name)

file.close()


#Task 2 - read entire file
file = open("students.txt", "r")

for name in file:
    print(name)

file.close()


#Task 3 - read into an array
file = open("students.txt", "r")

Students = []

for name in file:
    Students.append(name.strip())

file.close()

print(Students)


#Task 4 - create a new file
file = open("newstudents.txt", "w")

for i in range(5):
    name = input("Enter student name: ")
    file.write(name + "\n")

file.close()


#Task 5 - append a record 
name = input("Enter student name: ")

file = open("students.txt", "a")

file.write(name + "\n")

file.close()


#Task 6 - copy file
file = open("students.txt", "r")
backup = open("backup.txt", "w")

for name in file:
    backup.write(name)

file.close()
backup.close()


#Task 7 - create uppercase ver
file = open("students.txt", "r")
upper = open("upperstudents.txt", "w")

for name in file:
    upper.write(name.upper())

file.close()
upper.close()

#Task 8 - create numbered file
file = open("students.txt", "r")
numbered = open("numbered.txt", "w")

number = 1

for name in file:
    name = name.strip()
    numbered.write(str(number) + " " + name + "\n")
    number += 1

file.close()
numbered.close()


#Task 9 -  merge 2 files
with open("group1.txt", "r") as f1, open("group2.txt", "r") as f2:
    data = f1.read() + f2.read()

with open("allstudents.txt", "w") as f:
    f.write(data)


#Task 10 - remove a student
    name_to_remove = input("Enter the student name to remove: ")

with open("students.txt", "r") as f:
    records = f.readlines()

with open("students.txt", "w") as f:
    for record in records:
        if not record.startswith(name_to_remove):
            f.write(record)

#Task 11 - replace a student name
old_name = input("Enter the existing name: ")
new_name = input("Enter the replacement name: ")

with open("students.txt", "r") as file:
    records = file.readlines()

with open("students.txt", "w") as file:
    for record in records:
        name = record.strip()

        if name == old_name:
            file.write(new_name + "\n")
        else:
            file.write(record)

#Task 12 - create an audit report
with open("students.txt", "r") as file:
    names = file.readlines()

total_records = len(names)

with open("report.txt", "w") as file:
    file.write("Student Registration Report\n")
    file.write("--------------------------\n")
    file.write("Total records: " + str(total_records) + "\n")


#Task 13 - filter records
with open("students.txt", "r") as file:
    names = file.readlines()

with open("shortnames.txt", "w") as file:
    for name in names:
        name = name.strip()

        if len(name) < 5:
            file.write(name + "\n")

#Task 14 - reverse the file
with open("students.txt", "r") as file:
    names = file.readlines()

names.reverse()

with open("reversed.txt", "w") as file:
    for name in names:
        file.write(name)

#Task 15 - deduplicate file
with open("students.txt", "r") as file:
    names = file.readlines()

unique_names = []

for name in names:
    name = name.strip()

    if name not in unique_names:
        unique_names.append(name)

with open("unique.txt", "w") as file:
    for name in unique_names:
        file.write(name + "\n")
