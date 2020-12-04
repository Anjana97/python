students={"roll":100,"name":"ajay","course":"bca"}
# print(students["name"])
# print(students["course"])
for item in students:
    print(item,students[item])
    #or

for k,v in students.items():
    print (k,v)
students["name"]="AJAY"
print(students["name"])

#to check roll key in studets
print("roll" in students)

#check total in students else add add total(key,val) pair
if ("total" not in students):
    students["total"]=150
    print(students)

#to update the value
students["total"]+=50
print(students)