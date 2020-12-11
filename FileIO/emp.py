f=open("employee","r")
emp_dict={}
for lines in f:
    print(lines)#100,don,devop,2,25000
    id,name,desig,exp,sal=lines.rstrip("\n").split(",")
    if id not in emp_dict:
        emp_dict[id]={"id":id,"name":name,"desig":desig,"exp":exp,"sal":sal}
print(emp_dict)


