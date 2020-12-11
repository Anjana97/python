students={
    100:{"roll":100,"name":"ajay","total":140,"course":"bca"},
    101:{"roll":101,"name":"vijay","total":145,"course":"bca"},
    102:{"roll":102,"name":"majay","total":180,"course":"mca"},
    103:{"roll":103,"name":"najay","total":140,"course":"mca"}
}
print(students[100]) #{'roll': 100, 'name': 'ajay', 'total': 140, 'course': 'bca'}
#print name only
print(students[100]["name"]) #ajay
#print the total mark
print(students[100]["total"]) #140


def printStudent(**val):
    print(val)
    id=val.get("id")
    if id in students:
        print(students[id]["name"])
    else:
        print("student in this roll number doesn't exist")

printStudent(id=108)