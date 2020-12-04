#file operation Read r, Write w, Append A
#step1 create refernece
#refernce_name=open(filepath,mode_of_operation)
f=open("name","r")
lst=[]
for lines in f:
    lst.append(lines.rstrip("\n"))
print(lst)