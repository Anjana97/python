employees=[[1001,"ajay","qa",150000],
          [1002,"vijay","developer",25000],
          [1003,"arun","ba",150000],
          [1004,"amal","developer",300000]]

#print all employee id
for employee in employees:
    print(employee[0])
#find total of salary
totalsal=0
for employee in employees:
    totalsal+=employee[3]
print(totalsal)
#how many numbers working as developer
cnt=0
for employee in employees:
    if employee[2]=="developer":
        cnt+=1
print(cnt)
#find total salary group by designation
totalsaldev=totalsalba=totalsalqa=0
for employee in employees:
    if employee[2] == "qa":
        totalsalqa += employee[3]
    if employee[2]=="developer":
        totalsaldev += employee[3]
    if employee[2] == "ba":
        totalsalba+=employee[3]
print(totalsaldev)
print(totalsalba)
print(totalsalqa)
