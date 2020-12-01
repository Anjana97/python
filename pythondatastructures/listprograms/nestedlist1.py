students=[[1001,"ajay","mca",150],
          [1002,"vijay","bca",145],
          [1003,"arun","mca",150],
          [1004,"amal","bca",130]]
#print list
for student in students:
    print(student)
# print name only
for student in students:
    print(student[1])
    # ajay
    # vijay
    # arun
    # amal
#print all student roll number
for student in students:
    print(student[0])
#print all student details whose course="mca"
for student in students:
    if student[2]=="mca":
        print(student)
#print all student whose mark greater than 140
for student in students:
    if student[3]>140:
        print(student)

#find total sum of students total grup by course
totalm=totalb=0
for student in students:
    if student[2]=="mca":
        totalm+=student[3]
    elif student[2] == "bca":
            totalb+= student[3]
print("mca",totalm)
print("bca",totalb)


