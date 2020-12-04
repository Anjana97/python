employee={"eid":1001,"name":"anjana","designation":"hr","salary":5000}
#display emp name
print(employee["name"])
#check exp in emp, if not then add emp
print("exp" in employee)
if ("exp" not in employee):
    employee["exp"]=9
    print(employee)
#updte salary
employee["salary"]+=5000
print(employee["salary"])