employees=[[10001,"ajay","qa",1981,2003],
            [1002,"vijay","developer",1992,2000],
            [1003,"arun","ba",1989,2010],
            [1004,"amal","developer",2009,2014],
            [1005,"vimal","developer",1987,1989]]
temp=0
#print all employee desigination
for employee in employees:
    print(employee[2])

#print all employee whose desi= developer
for employee in employees:
    if employee[2]=="developer":
        print(employee[1])

#print all employees who were working in 1980s
for employee in employees:
    if employee[3]<1999:
        if employee[3]>1979:
            print(employee[1])
#print all employee details whose experience>9yrs

for employee in employees:
    if ((employee[4]-employee[3])>9):
        print(employee)