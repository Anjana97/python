f=open("data","r")
set1=set()
for lines in f:
    set1.add(lines.rstrip("\n"))
print(set1)